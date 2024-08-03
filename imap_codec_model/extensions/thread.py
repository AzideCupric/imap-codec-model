from __future__ import annotations
from typing import Literal

from imap_codec_model.core import StrOther, TaggedBase, NoZeroUint, Vec1, Vec2

class Members(TaggedBase):
    prefix: Vec1[NoZeroUint]
    answers: Vec2[ThreadType] | None # FIXME: 递归引用，可能无效，考虑修改为Any


class Nested(TaggedBase):
    answers: Vec2[ThreadType] # FIXME: 递归引用，可能无效，考虑修改为Any


ThreadType = Members | Nested

ThreadingAlgorithm = Literal[
    "OrderedSubject",
    "References",
] | StrOther
