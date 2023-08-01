# Author: Teon Brooks <teon.brooks@gmail.com>
#
# License: BSD (3-clause)
import math
from os import getenv, path as op
import time
import pytest

from mne.io import read_raw_fif
from mne.datasets import testing
import numpy as np

from mne_realtime import LSLClient, MockLSLStream
from mne_realtime.lsl_client import _check_pylsl_installed

base_dir = op.join(op.dirname(__file__), 'data')

host = 'myuid34234'
raw_fname = op.join(base_dir, 'test_raw.fif')


@testing.requires_testing_data
def test_lsl_client():
    """Test the LSLClient for connection and data retrieval."""
    pytest.importorskip('pylsl')
    raw = read_raw_fif(raw_fname)
    raw_info = raw.info
    sfreq = raw_info['sfreq']
    n_secs = 1
    n_requested_samples = math.ceil(sfreq * n_secs)
    with MockLSLStream(host, raw, ch_type='eeg', status=True):
        with LSLClient(info=raw_info, host=host, wait_max=5) as client:
            client_info = client.get_measurement_info()
            epoch = client.get_data_as_epoch(n_samples=n_requested_samples)

            epoch_data = epoch.get_data()
            n_epochs, n_channels, n_times = epoch_data.shape
            assert n_epochs == 1
            assert n_channels == client_info['nchan']
            assert n_times == n_requested_samples

    assert client_info['nchan'] == raw_info['nchan']
    assert ([ch["ch_name"] for ch in client_info["chs"]] ==
            [ch_name for ch_name in raw_info['ch_names']])

    assert raw_info['nchan'], sfreq == epoch.get_data().shape[1:]


@testing.requires_testing_data
def test_lsl_client_nodata():
    """Test that LSLClient gracefully handles no-data from LSL."""
    pytest.importorskip('pylsl')
    raw = read_raw_fif(raw_fname)
    raw_info = raw.info
    with MockLSLStream(host, raw, ch_type='eeg', status=True):
        with LSLClient(info=raw_info, host=host, wait_max=5) as client:
            epoch = client.get_data_as_epoch(n_samples=0, timeout=0)
            assert epoch is None


def test_connect(monkeypatch):
    """Mock connect to LSL stream."""
    # Import pylsl here so that the test can be skipped if pylsl is not installed
    pylsl = pytest.importorskip("pylsl")

    # Constants
    buffer_size = 17
    n_channels = 6
    c_channel_format = pylsl.cf_float32
    numpy_channel_format = np.float32

    # Replace pylsl streams with a mock
    monkeypatch.setattr(
        'pylsl.resolve_streams',
        lambda *args, **kwargs: [
            pylsl.StreamInfo(
                source_id=host,
                channel_count=n_channels,
                channel_format=c_channel_format,
            )
        ],
    )
    lsl_client = LSLClient(host=host, buffer_size=buffer_size)
    # Mock out the pylsl.resolve_streams
    lsl_client._connect()

    assert isinstance(lsl_client.client, pylsl.StreamInlet)
    assert lsl_client.buffer.shape == (buffer_size, n_channels)
    assert lsl_client.buffer.dtype == numpy_channel_format
