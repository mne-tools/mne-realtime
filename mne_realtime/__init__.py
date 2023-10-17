"""Realtime MEG data processing with servers and clients."""

# Authors: Christoph Dinh <chdinh@nmr.mgh.harvard.edu>
#          Martin Luessi <mluessi@nmr.mgh.harvard.edu>
#          Mainak Jas <mainakjas@gmail.com>
#          Matti Hamalainen <msh@nmr.mgh.harvard.edu>
#          Teon Brooks <teon.brooks@gmail.com>
#
# License: BSD (3-clause)

from warnings import warn

from ._version import __version__
from .client import RtClient
from .epochs import RtEpochs
from .lsl_client import LSLClient
from .mock_lsl_stream import MockLSLStream
from .mock_client import MockRtClient
from .stim_server_client import StimServer, StimClient
from .fieldtrip_client import FieldTripClient

warn(
    "MNE-realtime is discontinued in favor of the Lab Streaming Layer real-time "
    "interface availabe in MNE-lsl: https://mne.tools/mne-lsl/",
    FutureWarning,
    stacklevel=2,
)

__all__ = [
    "__version__",
    "FieldTripClient",
    "LSLClient",
    "MockLSLStream",
    "MockRtClient",
    "RtClient",
    "RtEpochs",
    "StimClient",
    "StimServer",
]
