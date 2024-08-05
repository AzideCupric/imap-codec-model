from typing import Literal
from .core import NoZeroUint, TaggedBase, Base, Vec1

class Value(Base):
    value: NoZeroUint

SeqOrUid = Value | Literal["Asterisk"]

class Single(TaggedBase):
    codec_data: SeqOrUid

class Range(TaggedBase):
    codec_data: tuple[SeqOrUid, SeqOrUid]

Sequence = Single | Range


SequenceSet = Vec1[Sequence]
