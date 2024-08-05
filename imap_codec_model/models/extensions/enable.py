from typing import Literal

from ..core import StrOther

CapabilityEnable = Literal["Utf8", "CondStore", "Metadata", "MetadataServer"] | StrOther
