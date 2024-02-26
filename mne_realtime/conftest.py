# -*- coding: utf-8 -*-
# Author: Eric Larson <larson.eric.d@gmail.com>
#
# License: BSD (3-clause)

import warnings
import pytest


def pytest_configure(config):
    """Configure pytest options."""
    # Fixtures
    for fixture in ('matplotlib_config',):
        config.addinivalue_line('usefixtures', fixture)

    # Marks
    for marker in (
        "network_test",
    ):
        config.addinivalue_line("markers", marker)

    # Warnings
    # - Once SciPy updates not to have non-integer and non-tuple errors (1.2.0)
    #   we should remove them from here.
    # - This list should also be considered alongside reset_warnings in
    #   doc/conf.py.
    warning_lines = r"""
    error::
    ignore:.*may indicate binary incompatibility.*:RuntimeWarning
    ignore:.*distutils Version classes are deprecated.*:
    ignore:`np.MachAr` is deprecated.*:DeprecationWarning
    ignore:mne\.io\.pick\..* is deprecated.*:FutureWarning
    ignore:The current default of copy=False will change.*:FutureWarning
    ignore:MNE-realtime is discontinued in favor of.*:FutureWarning
    ignore:unclosed .*:ResourceWarning
    """  # noqa: E501
    for warning_line in warning_lines.split('\n'):
        warning_line = warning_line.strip()
        if warning_line and not warning_line.startswith('#'):
            config.addinivalue_line('filterwarnings', warning_line)


@pytest.fixture(scope='session')
def matplotlib_config():
    """Configure matplotlib for viz tests."""
    import matplotlib
    # "force" should not really be necessary but should not hurt
    kwargs = dict()
    with warnings.catch_warnings(record=True):  # ignore warning
        warnings.filterwarnings('ignore')
        matplotlib.use('agg', force=True, **kwargs)  # don't pop up windows
    import matplotlib.pyplot as plt
    assert plt.get_backend() == 'agg'
    # overwrite some params that can horribly slow down tests that
    # users might have changed locally (but should not otherwise affect
    # functionality)
    plt.ioff()
    plt.rcParams['figure.dpi'] = 100
