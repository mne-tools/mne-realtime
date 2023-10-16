.. -*- mode: rst -*-

MNE-realtime
============

> [!WARNING]
> This project is discontinued in favor of [MNE-LSL](https://github.com/mne-tools/mne-lsl). At the moment, [MNE-LSL](https://github.com/mne-tools/mne-lsl) replaces the ``LSLClient`` and does not yet support the FieldTrip buffer.

This is a package for realtime analysis of MEG/EEG data with MNE. The documentation can be found here:

* `Examples`_
* `API`_

Dependencies
------------

* `numpy`_
* `scipy`_
* `MNE`_

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

   $ pip install https://api.github.com/repos/mne-tools/mne-realtime/zipball/main

These ``pip`` commands also work if you want to upgrade if a newer version of
``mne-realtime`` is available. If you do not have administrator privileges on the
computer, use the ``--user`` flag with ``pip``.

Quickstart
----------

.. code-block:: python

    info = mne.io.read_info(op.join(data_path, 'MEG', 'sample',
                            'sample_audvis_raw.fif'))
    with FieldTripClient(host='localhost', port=1972,
                         tmax=30, wait_max=5, info=info) as rt_client:
        rt_epochs = RtEpochs(rt_client, event_id, tmin, tmax, ...)
        rt_epochs.start()
        for ev in rt_epochs.iter_evoked():
            epoch_data = ev.data

        # or alternatively, get last n_samples
        rt_epoch = rt_client.get_data_as_epoch(n_samples=500)
        continuous_data = rt_epoch.get_data()

The ``FieldTripClient`` supports `multiple vendors through the FieldTrip buffer <http://www.fieldtriptoolbox.org/development/realtime/implementation/>`_.
It can be replaced with other clients such as ``LSLClient``. See `API`_ for a list of clients.

Bug reports
-----------

Use the `github issue tracker <https://github.com/mne-tools/mne-realtime/issues>`_
to report bugs.

.. _Examples: https://mne.tools/mne-realtime/auto_examples/index.html
.. _API: https://mne.tools/mne-realtime/api.html
.. _numpy: https://numpy.org
.. _scipy: https://scipy.org
.. _MNE: https://mne.tools
