from typing import Literal
from .core import TaggedBase, StrOther

Utf8Kind = Literal["Accept", "Only"]


class Utf8(TaggedBase):
    codec_data: Utf8Kind


CapabilityEnable = Utf8 | Literal["Condstore", "Metadata", "MetadataServer"] | StrOther
