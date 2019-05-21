# -*- coding: utf-8 -*-
#
# project-template documentation build configuration file, created by
# sphinx-quickstart on Mon Jan 18 14:44:12 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import date
from distutils.version import LooseVersion
import gc
import os
import os.path as op
import sys
import warnings

import sphinx
import sphinx_rtd_theme
import sphinx_gallery  # noqa
from sphinx_gallery.sorting import FileNameSortKey
from numpydoc import docscrape
import mne  # noqa
from mne_realtime import __version__

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'numpydoc',
    'sphinx_gallery.gen_gallery',
]

# this is needed for some reason...
# see https://github.com/numpy/numpydoc/issues/69
numpydoc_show_class_members = False

# pngmath / imgmath compatibility layer for different sphinx versions
if LooseVersion(sphinx.__version__) < LooseVersion('1.4'):
    extensions.append('sphinx.ext.pngmath')
else:
    extensions.append('sphinx.ext.imgmath')

autosummary_generate = True
autodoc_default_options = {'inherited-members': None}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# Generate the plots for the gallery
# plot_gallery = True

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'MNE-Realtime'
td = date.today()
copyright = u'2012-%s, MNE Developers. Last updated on %s' % (td.year,
                                                              td.isoformat())

nitpicky = True
suppress_warnings = ['image.nonlocal_uri']  # we intentionally link outside

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '_templates']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "autolink"

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Custom style
html_style = 'css/project-template.css'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['mne_realtime.']

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/mne_logo_small.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
html_copy_source = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'mne-realtime-doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  # ('index', 'project-template.tex', u'project-template Documentation',
  #  u'Vighnesh Birodkar', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = []

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = []

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://www.numpy.org/devdocs', None),
    'scipy': ('https://scipy.github.io/devdocs', None),
    'matplotlib': ('https://matplotlib.org', None),
    'sklearn': ('https://scikit-learn.org/stable', None),
    'joblib': ('https://joblib.readthedocs.io/en/latest', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
    'mne': ('https://mne-tools.github.io/dev', None),
}

##############################################################################
# sphinx-gallery

examples_dirs = ['../examples']
gallery_dirs = ['auto_examples']


scrapers = ('matplotlib',)


class Resetter(object):
    """Simple class to make the str(obj) static for Sphinx build env hash."""

    def __repr__(self):
        return '<%s>' % (self.__class__.__name__,)

    def __call__(self, gallery_conf, fname):
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
    # restrict
    warnings.filterwarnings('error')
    # allow these, but show them
    warnings.filterwarnings('default', module='sphinx')  # internal warnings
    # allow these warnings, but don't show them
    warnings.filterwarnings('ignore', '.*is currently using agg.*')
    for key in ('HasTraits', r'numpy\.testing', 'importlib', r'np\.loads',
                'Using or importing the ABCs from',  # internal modules on 3.7
                "DocumenterBridge requires a state object",  # sphinx dev
                "'U' mode is deprecated",  # sphinx io
                ):
        warnings.filterwarnings(  # deal with other modules having bad imports
            'ignore', message=".*%s.*" % key, category=DeprecationWarning)
    warnings.filterwarnings(  # deal with other modules having bad imports
        'ignore', message=".*ufunc size changed.*", category=RuntimeWarning)
    warnings.filterwarnings(  # realtime
        'ignore', message=".*unclosed file.*", category=ResourceWarning)
    warnings.filterwarnings('ignore', message='Exception ignored in.*')
    # allow this ImportWarning, but don't show it
    warnings.filterwarnings(
        'ignore', message="can't resolve package from", category=ImportWarning)


reset_warnings(None, None)
sphinx_gallery_conf = {
    'doc_module': 'mne_realtime',
    'reference_url': dict(mne_realtime=None),
    'examples_dirs': examples_dirs,
    'default_thumb_file': os.path.join('_static', 'mne_helmet.png'),
    'backreferences_dir': 'generated',
    'plot_gallery': 'True',  # Avoid annoying Unicode/bool default warning
    'download_section_examples': False,
    'thumbnail_size': (160, 112),
    'min_reported_time': 1.,
    'abort_on_example_error': False,
    'reset_modules': ('matplotlib', Resetter()),  # called w/each script
    'image_scrapers': scrapers,
    'show_memory': True,
    'line_numbers': False,  # XXX currently (0.3.dev0) messes with style
    'within_subsection_order': FileNameSortKey,
    'junit': op.join('..', 'test-results', 'sphinx-gallery', 'junit.xml'),
}

##############################################################################
# numpydoc

# XXX This hack defines what extra methods numpydoc will document
docscrape.ClassDoc.extra_public_methods = mne.utils._doc_special_members
numpydoc_class_members_toctree = False
numpydoc_attributes_as_param_list = False
numpydoc_xref_param_type = True
numpydoc_xref_aliases = {
    # Matplotlib
    'colormap': ':doc:`colormap <matplotlib:tutorials/colors/colormaps>`',
    'color': ':doc:`color <matplotlib:api/colors_api>`',
    'Axes': 'matplotlib.axes.Axes',
    'Figure': 'matplotlib.figure.Figure',
    'Axes3D': 'mpl_toolkits.mplot3d.axes3d.Axes3D',
    # MNE
    'Epochs': 'mne.Epochs', 'Layout': 'mne.channels.Layout',
    'Raw': 'mne.io.Raw', 'Covariance': 'mne.Covariance',
    'Evoked': 'mne.Evoked', 'Info': 'mne.Info',
    'Montage': 'mne.channels.Montage',
    'DigMontage': 'mne.channels.DigMontage',
    # mne_realtime
    'RtEpochs': 'mne_realtime.RtEpochs',
}
numpydoc_xref_ignore = {
    # words
    'instance', 'instances', 'of', 'default', 'shape', 'or',
    'with', 'length', 'pair', 'matplotlib', 'optional', 'kwargs', 'in',
    'dtype', 'object', 'self.verbose',
    # shapes
    'n_channels', 'n_times', 'nchan', 'n_epochs', 'n_events', 'n_picks',
    'n_ch_groups',
}


##############################################################################

def setup(app):
    # a copy button to copy snippet of code from the documentation
    app.add_js_file('js/copybutton.js')
