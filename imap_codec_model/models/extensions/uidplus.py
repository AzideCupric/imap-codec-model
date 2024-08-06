from ..core import Vec1, NoZeroUint, TaggedBase


class Single(TaggedBase):
    codec_data: NoZeroUint


class Range(TaggedBase):
    codec_data: tuple[NoZeroUint, NoZeroUint]


UidElement = Single | Range

UidSet = Vec1[UidElement]
