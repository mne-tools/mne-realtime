# Authors: Teon Brooks <teon.brooks@gmail.com>
#          Mainak Jas <mainakjas@gmail.com>
#
# License: BSD (3-clause)

import ctypes
import numpy as np

from .base_client import _BaseClient
from mne.epochs import EpochsArray
from mne.io.meas_info import create_info
from mne.io.pick import _picks_to_idx, pick_info
from mne.utils import fill_doc


class LSLClient(_BaseClient):
    """LSL Realtime Client.

    Parameters
    ----------
    info : instance of mne.Info | None
        The measurement info read in from a file. If None, it is generated from
        the LSL stream. This method may result in less info than expected.
        Also, the channel type of the LSL stream must be one the MNE supported
        channel types: ‘ecg’, ‘bio’, ‘stim’, ‘eog’, ‘misc’, ‘seeg’,
        ‘ecog’, ‘mag’, ‘eeg’, ‘ref_meg’, ‘grad’, ‘emg’, ‘hbr’ or ‘hbo’.
        If the channel type is EEG, the `standard_1005` montage is used for
        electrode location.
    host : str
        The LSL identifier of the server. This is the source_id designated
        when the LSL stream was created. Make sure the source_id is unique on
        the LSL subnet. For more information on LSL, please check the
        docstrings on `StreamInfo` and `StreamInlet` in the pylsl.
    port : int | None
        Port to use for the connection.
    wait_max : float
        Maximum time (in seconds) to wait for real-time buffer to start
    tmin : float | None
        Time instant to start receiving buffers. If None, start from the latest
        samples available.
    tmax : float
        Time instant to stop receiving buffers.
    buffer_size : int
        Size of each buffer in terms of number of samples.
    verbose : bool, str, int, or None
        If not None, override default verbose level (see :func:`mne.verbose`
        for more).
    """

    @fill_doc
    def get_data_as_epoch(self, n_samples=1024, picks=None):
        """Return last n_samples from current time.

        Parameters
        ----------
        n_samples : int
            Number of samples to fetch.
        %(picks_all)s

        Returns
        -------
        epoch : instance of Epochs
            The samples fetched as an Epochs object.

        See Also
        --------
        mne.Epochs.iter_evoked
        """
        # set up timeout in case LSL process hang. wait arb 5x expected time
        wait_time = n_samples * 5. / self.info['sfreq']

        # create an event at the start of the data collection
        events = np.expand_dims(np.array([0, 1, 1]), axis=0)
        _, timestamps = self.client.pull_chunk(
            max_samples=min(n_samples, self.buffer.shape[0]),
            timeout=wait_time,
            dest_obj=self.buffer,
        )
        num_timestamps = len(timestamps) if timestamps else 0
        data = self.buffer[:len(timestamps), :]

        picks = _picks_to_idx(self.info, picks, 'all', exclude=())
        info = pick_info(self.info, picks)
        return EpochsArray(data[picks][np.newaxis], info, events)

    def iter_raw_buffers(self):
        """Return an infinite iterator over raw buffers."""
        while True:
            _, timestamps = self.client.pull_chunk(
                max_samples=self.buffer.shape[0],
                dest_obj=self.buffer,
            )
            num_timestamps = len(timestamps) if timestamps else 0
            data = self.buffer[:len(timestamps), :]
            yield data.copy()

    def _connect(self):
        # To use this function with an LSL stream which has a 'name' but no
        # 'source_id', change the keyword in pylsl.resolve_byprop accordingly.
        pylsl = _check_pylsl_installed(strict=True)
        print(f'Looking for LSL stream {self.host}...')
        # resolve_byprop is a bit fragile
        streams = pylsl.resolve_streams(wait_time=min(0.1, self.wait_max))
        ids = list()
        for stream_info in streams:
            ids.append(stream_info.source_id())
            if ids[-1] == self.host:
                break
        else:
            raise RuntimeError(f'{self.host} not found in streams: {ids}')
        print(f'Found stream {repr(stream_info.name())} via '
              f'{stream_info.source_id()}...')
        self.client = pylsl.StreamInlet(info=stream_info,
                                        max_buflen=self.buffer_size)
        # Most ctypes can be converted to numpy dtypes.
        # Exceptions include c_char_p
        value_type = pylsl.pylsl.fmt2type[stream_info.channel_format()]
        if value_type == ctypes.c_char_p:
            value_type = None
        self.buffer = np.empty(
            (self.buffer_size, stream_info.channel_count()),
            dtype=value_type,
        )

        return self

    def _connection_error(self):
        pylsl = _check_pylsl_installed(strict=True)
        extra = (f' Available streams on {self.host} from resolve_streams():\n'
                 f'{pylsl.resolve_streams()}')
        super()._connection_error(extra)

    def _create_info(self):
        montage = None
        sfreq = self.client.info().nominal_srate()

        lsl_info = self.client.info()
        ch_info = lsl_info.desc().child("channels").child("channel")
        ch_names = list()
        ch_types = list()
        ch_type = lsl_info.type().lower()
        for k in range(1,  lsl_info.channel_count() + 1):
            ch_names.append(ch_info.child_value("label") or
                            '{} {:03d}'.format(ch_type.upper(), k))
            ch_types.append(ch_info.child_value("type").lower() or ch_type)
            ch_info = ch_info.next_sibling()
        if ch_type == "eeg":
            info = create_info(ch_names, sfreq, ch_types)
            try:
                info.set_montage('standard_1005', match_case=False)
            except ValueError:
                pass

        return info

    def _disconnect(self):
        self.client.close_stream()

        return self


def _check_pylsl_installed(strict=True):
    """Aux function."""
    try:
        import pylsl
        return pylsl
    except ImportError:
        if strict is True:
            raise RuntimeError('For this functionality to work, the pylsl '
                               'library is required.')
        else:
            return False
