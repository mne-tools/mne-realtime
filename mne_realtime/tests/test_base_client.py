# Author: Charles Guan <charles@ae.studio>
#
# License: BSD (3-clause)

import pytest

from mne_realtime.base_client import _BaseClient


def test_base_client():
    """Initialize _BaseClient as context manager."""
    with _BaseClient() as client:
        pass


def test_base_client_propagate_exception():
    """_BaseClient propagates exceptions to user."""
    with pytest.raises(Exception):
        with _BaseClient() as client:
            raise Exception
