#! /usr/bin/env python
"""A module for real-time data analysis with MNE."""

import codecs
import os

from setuptools import find_packages, setup

# get __version__ from _version.py
ver_file = os.path.join('mne_realtime', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = 'mne-realtime'
DESCRIPTION = 'A module for real-time data analysis with MNE.'
with codecs.open('README.md', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'Teon Brooks'
MAINTAINER_EMAIL = 'teon.brooks@gmail.com'
URL = 'https://github.com/mne-tools/mne-realtime'
LICENSE = 'new BSD'
DOWNLOAD_URL = 'https://github.com/mne-tools/mne-realtime'
VERSION = __version__
INSTALL_REQUIRES = ['numpy', 'scipy', 'mne>=1.0.0']
CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 3.8',
               'Programming Language :: Python :: 3.9',
               'Programming Language :: Python :: 3.10',
               'Programming Language :: Python :: 3.11',
               ]
EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov',
    ],
    'docs': [
        'sphinx',
        'sphinx-gallery',
        'pydata-sphinx-theme',
        'sphinx_copybutton',
        'sphinxcontrib-bibtex',
        'numpydoc',
        'matplotlib',
        'memory_profiler',
    ]
}

setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      zip_safe=False,  # the package can run out of an .egg file
      classifiers=CLASSIFIERS,
      packages=find_packages(),
      python_requires='>=3.8',
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE)
