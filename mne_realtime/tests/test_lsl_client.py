# Author: Teon Brooks <teon.brooks@gmail.com>
#
# License: BSD (3-clause)
import math
from os import getenv, path as op
import time
import pytest

from mne.utils import requires_pylsl
from mne.io import read_raw_fif
from mne.datasets import testing
import numpy as np
import pylsl

from mne_realtime import LSLClient, MockLSLStream

base_dir = op.join(op.dirname(__file__), 'data')

host = 'myuid34234'
raw_fname = op.join(base_dir, 'test_raw.fif')


@requires_pylsl
@testing.requires_testing_data
def test_lsl_client():
    """Test the LSLClient for connection and data retrieval."""
    raw = read_raw_fif(raw_fname)
    n_secs = 1
    raw.crop(tmin=0, tmax=n_secs)
    raw_info = raw.info
    sfreq = raw_info['sfreq']
    with MockLSLStream(host, raw, ch_type='eeg', status=True):
        with LSLClient(info=raw_info, host=host, wait_max=5) as client:
            client_info = client.get_measurement_info()
            n_samples = math.ceil(sfreq * n_secs * 2)
            epoch = client.get_data_as_epoch(n_samples=n_samples)

            epoch_data = epoch.get_data()
            n_epochs, n_channels, n_times = epoch_data.shape
            assert n_epochs == 1
            assert n_channels == client_info['nchan']

    assert client_info['nchan'] == raw_info['nchan']
    assert ([ch["ch_name"] for ch in client_info["chs"]] ==
            [ch_name for ch_name in raw_info['ch_names']])

    assert raw_info['nchan'], sfreq == epoch.get_data().shape[1:]

def test_connect(mocker):
    """Mock connect to LSL stream."""
    # Constants
    buffer_size = 17
    n_channels = 6
    c_channel_format = pylsl.cf_float32
    numpy_channel_format = np.float32

    # Replace pylsl streams with a mock
    mock_resolve_streams = mocker.patch(
        'pylsl.resolve_streams',
        return_value=[pylsl.StreamInfo(
            source_id=host,
            channel_count=n_channels,
            channel_format=c_channel_format,
        )],
    )

    lsl_client = LSLClient(host=host, buffer_size=buffer_size)
    # Mock out the pylsl.resolve_streams
    lsl_client._connect()

    assert isinstance(lsl_client.client, pylsl.StreamInlet)
    assert lsl_client.buffer.shape == (buffer_size, n_channels)
    assert lsl_client.buffer.dtype == numpy_channel_format
