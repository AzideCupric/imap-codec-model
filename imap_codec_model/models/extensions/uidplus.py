from ..core import NoZeroUint, TaggedBase, Vec1


class Single(TaggedBase):
    codec_data: NoZeroUint

class Range(TaggedBase):
    codec_data: tuple[NoZeroUint, NoZeroUint]


UidElement = Single | Range

UidSet = Vec1[UidElement]
"""Uid集合，至少包含一个UidElement"""
