from typing import Literal

from .core import Tagged


class LongEntry(Tagged):
    codec_data: int


class MaxSize(Tagged):
    codec_data: int


MetadataCode = (
    Literal[
        "TooMany",
        "NoPrivate",
    ]
    | LongEntry
    | MaxSize
)
