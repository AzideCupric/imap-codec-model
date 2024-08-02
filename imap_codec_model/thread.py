from __future__ import annotations
from typing import Literal

from .core import StrOther, TaggedBase, Base, NoZeroUint, Vec1, Vec2

class Members(TaggedBase):
    class MemberVal(Base):
        prefix: Vec1[NoZeroUint]
        answers: Vec2[ThreadType] | None # FIXME: 递归引用，可能无效，考虑修改为Any

    codec_data: MemberVal

class Nested(TaggedBase):
    class NestedVal(Base):
        answers: Vec2[ThreadType] # FIXME: 递归引用，可能无效，考虑修改为Any

    codec_data: NestedVal

ThreadType = Members | Nested

ThreadingAlgorithm = Literal[
    "OrderedSubject",
    "References",
] | StrOther

