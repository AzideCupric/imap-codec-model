from typing import Annotated, Literal, TypeVar
from collections.abc import Sequence

from msgspec import Struct, Meta

T = TypeVar("T")

Base = Struct
"""为非CodecModel的基类"""


class TaggedBase(Struct, tag_field="codec_model"):
    """为CodecModel的基类，tag_field指定了tag字段的名称为codec_model: <class name>，
    继承时不需要显式指定tag_field和codec_model字段
    """
    pass


class Atom(TaggedBase):
    codec_data: str


class Quoted(TaggedBase):
    codec_data: str

LiteralMode = Literal["Sync", "NonSync"]

class LiteralType(TaggedBase, tag="Literal"):
    data: Sequence[int]
    mode: LiteralMode


IString = Quoted | LiteralType

class String(TaggedBase):
    codec_data: IString

AString = Atom | String
NString = IString | None

Charset = Atom | Quoted

NoZeroUint = Annotated[int, Meta(gt=0)]
"""大于0的整数"""

Uint = Annotated[int, Meta(ge=0)]

QuotedChar = Annotated[str, Meta(max_length=1)]
"""引号内的长度为1的字符串（字符）"""

Vec1 = Annotated[Sequence[T], Meta(min_length=1)]
"""至少包含一个元素的序列"""

Vec2 = Annotated[Sequence[T], Meta(min_length=2)]
"""至少包含两个元素的序列"""

class StrOther(TaggedBase, tag="Other"):
    codec_data: str
