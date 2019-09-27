.. -*- mode: rst -*-

|Travis|_ |Azure|_ |CircleCI|_ |Codecov|_

.. |Travis| image:: https://travis-ci.com/mne-tools/mne-realtime.svg?branch=master
.. _Travis: https://travis-ci.com/mne-tools/mne-realtime/branches

.. |Azure| image:: https://dev.azure.com/mne-tools/mne-realtime/_apis/build/status/mne-tools.mne-realtime?branchName=master
.. _Azure: https://dev.azure.com/mne-tools/mne-realtime/_build/latest?definitionId=1&branchName=master

.. |CircleCI| image:: https://circleci.com/gh/mne-tools/mne-realtime.svg?style=svg
.. _CircleCI: https://circleci.com/gh/mne-tools/mne-realtime

.. |Codecov| image:: https://codecov.io/gh/mne-tools/mne-realtime/branch/master/graph/badge.svg
.. _Codecov: https://codecov.io/gh/mne-tools/mne-realtime

MNE-realtime
============

This is a repository for realtime analysis of MEG/EEG data with MNE. The documentation can be found here:

   * `Examples <auto_examples/index.html>`_
   * `API <api.html>`_

Dependencies
~~~~~~~~~~~~

* numpy
* MNE

Installation
------------

We recommend the Anaconda Python distribution. We require that you use Python 3. You may choose to install mne-realtime via pip.

Besides ``numpy`` and ``scipy`` (which are included in the standard Anaconda
installation), you will need to install the most recent version of ``MNE``
using the ``pip`` tool:

.. code-block:: bash

   $ pip install -U mne


Then install ``mne-realtime``:

.. code-block:: bash

   $ pip install https://api.github.com/repos/mne-tools/mne-realtime/zipball/master

These ``pip`` commands also work if you want to upgrade if a newer version of
``mne-realtime`` is available. If you do not have administrator privileges on the
computer, use the ``--user`` flag with ``pip``.

Bug reports
-----------

Use the `github issue tracker <https://github.com/mne-tools/mne-realtime/issues>`_
to report bugs.
