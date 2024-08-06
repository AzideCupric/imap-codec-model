from collections.abc import Sequence
from typing import Literal, TypeVar, Annotated

from msgspec import Meta, Struct

T = TypeVar("T")

Base = Struct
"""Base class for non-CodecModel structures."""


class TaggedBase(Struct, tag_field="codec_model"):
    """Base class for CodecModel structures. The `tag_field` specifies that
    the tag field name is `codec_model: <class name>`.
    When inheriting, you do not need to explicitly specify the `tag_field`
    or `codec_model` fields.
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
"""An integer greater than 0."""

Uint = Annotated[int, Meta(ge=0)]
"""An integer greater than or equal to 0."""

QuotedChar = Annotated[str, Meta(max_length=1)]
"""A string (character) of length 1 enclosed in quotes."""

Vec1 = Annotated[Sequence[T], Meta(min_length=1)]
"""A sequence containing at least one element."""

Vec2 = Annotated[Sequence[T], Meta(min_length=2)]
"""A sequence containing at least two elements."""


class StrOther(TaggedBase, tag="Other"):
    codec_data: str
