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
    raw.crop(n_secs)
    raw_info = raw.info
    sfreq = raw_info['sfreq']
    with MockLSLStream(host, raw, ch_type='eeg', status=True):
        with LSLClient(info=raw_info, host=host, wait_max=5) as client:
            client_info = client.get_measurement_info()
            n_samples = math.ceil(sfreq * n_secs * 2)
            epoch = client.get_data_as_epoch(n_samples=n_samples)
            time.sleep(1.)
            raw = list(client.iter_raw_buffers())
            assert len(raw) > 0

    assert client_info['nchan'] == raw_info['nchan']
    assert ([ch["ch_name"] for ch in client_info["chs"]] ==
            [ch_name for ch_name in raw_info['ch_names']])

    assert raw_info['nchan'], sfreq == epoch.get_data().shape[1:]
