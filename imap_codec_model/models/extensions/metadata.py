from typing import Literal

from ..core import AString, LiteralType, NString, TaggedBase, Uint, Vec1


class LongEntry(TaggedBase):
    codec_data: Uint


class MaxSize(TaggedBase):
    codec_data: Uint


MetadataCode = (
    Literal[
        "TooMany",
        "NoPrivate",
    ]
    | LongEntry
    | MaxSize
)

class EntryValue(TaggedBase):
    entry: AString
    value: NString | LiteralType

class WithValues(TaggedBase):
    codec_data: Vec1[EntryValue]

class WithoutValues(TaggedBase):
    codec_data: Vec1[AString]

MetadataResponse = WithValues | WithoutValues

Depth = Literal["Null", "One", "Infinity"]

GetMetadataOption = MaxSize | Depth
