from typing import Literal

from imap_codec_model.core import AString, LiteralType, NString, TaggedBase, Uint, Vec1


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

MetadataResponse = Vec1[EntryValue] | Vec1[AString]

Depth = Literal["Null", "One", "Infinity"]

GetMetadataOption = MaxSize | Depth
