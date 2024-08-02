from typing import Literal

from imap_codec_model.core import StrOther

CapabilityEnable = Literal["Utf8", "CondStore", "Metadata", "MetadataServer"] | StrOther
