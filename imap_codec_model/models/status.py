from typing import Literal

from .core import Uint, NoZeroUint, TaggedBase


class Messages(TaggedBase):
    codec_data: Uint


class Recent(TaggedBase):
    codec_data: Uint


class UidNext(TaggedBase):
    codec_data: NoZeroUint


class UidValidity(TaggedBase):
    codec_data: NoZeroUint


class Unseen(TaggedBase):
    codec_data: Uint


class Deleted(TaggedBase):
    codec_data: Uint


class DeletedStorage(TaggedBase):
    codec_data: Uint


StatusDataItem = Messages | Recent | UidNext | UidValidity | Unseen | Deleted | DeletedStorage

StatusDataItemName = Literal[
    "Messages",
    "Recent",
    "UidNext",
    "UidValidity",
    "Unseen",
    "Deleted",
    "DeletedStorage",
    "HighestModSeq",
]
