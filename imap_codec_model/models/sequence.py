from typing import Literal
from .core import NoZeroUint, TaggedBase, Vec1

class Value(TaggedBase):
    codec_data: NoZeroUint

SeqOrUid = Value | Literal["Asterisk"]

class Single(TaggedBase):
    codec_data: SeqOrUid

class Range(TaggedBase):
    codec_data: tuple[SeqOrUid, SeqOrUid]

Sequence = Single | Range


SequenceSet = Vec1[Sequence]
