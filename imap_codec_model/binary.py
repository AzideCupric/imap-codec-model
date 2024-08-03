from .core import LiteralType, TaggedBase


class Literal(TaggedBase):
    codec_data: LiteralType


class Literal8(TaggedBase):
    codec_data: LiteralType

LiteralOrLiteral8 = Literal | Literal8
