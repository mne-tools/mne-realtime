import gc
import warnings


def reset(gallery_conf, fname):
    import matplotlib.pyplot as plt
    reset_warnings(gallery_conf, fname)
    # in case users have interactive mode turned on in matplotlibrc,
    # turn it off here (otherwise the build can be very slow)
    plt.ioff()
    gc.collect()


def reset_warnings(gallery_conf, fname):
    """Ensure we are future compatible and ignore silly warnings."""
    # In principle, our examples should produce no warnings.
    # Here we cause warnings to become errors, with a few exceptions.
    # This list should be considered alongside
    # setup.cfg -> [tool:pytest] -> filterwarnings

    # remove tweaks from other module imports or example runs
    warnings.resetwarnings()
    # allow warnings now that mne-realtime is deprecated
    warnings.filterwarnings('always')
    # allow these, but show them
    warnings.filterwarnings('default', module='sphinx')  # internal warnings
    # allow these warnings, but don't show them
    warnings.filterwarnings('ignore', '.*is currently using agg.*')
    for key in ('HasTraits', r'numpy\.testing', 'importlib', r'np\.loads',
                'Using or importing the ABCs from',  # internal modules on 3.7
                "DocumenterBridge requires a state object",  # sphinx dev
                "'U' mode is deprecated",  # sphinx io
                'pkg_resources is deprecated as an API',  # bibtex
                'Deprecated call to `pkg_resources',
                ):
        warnings.filterwarnings(  # deal with other modules having bad imports
            'ignore', message=".*%s.*" % key, category=DeprecationWarning)
    warnings.filterwarnings(
        "ignore",
        message=".*is non-interactive, and thus cannot.*",
    )
    warnings.filterwarnings(  # deal with other modules having bad imports
        'ignore', message=".*ufunc size changed.*", category=RuntimeWarning)
    warnings.filterwarnings(  # realtime
        'ignore', message=".*unclosed file.*", category=ResourceWarning)
    warnings.filterwarnings(
        'ignore', message='The str interface for _CascadingStyleSheet.*')
    warnings.filterwarnings('ignore', message='Exception ignored in.*')
    # allow this ImportWarning, but don't show it
    warnings.filterwarnings(
        'ignore', message="can't resolve package from", category=ImportWarning)
