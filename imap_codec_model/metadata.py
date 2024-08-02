from typing import Literal

from .core import AString, Base, LiteralType, NString, TaggedBase, Uint, Vec1


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
    class EntryValueVal(Base):
        entry: AString
        value: NString | LiteralType

    codec_data: EntryValueVal

MetadataResponse = Vec1[EntryValue] | Vec1[AString]

Depth = Literal["Null", "One", "Infinity"]

GetMetadataOption = MaxSize | Depth
