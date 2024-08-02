from collections.abc import Sequence
from datetime import datetime
from typing import Literal

from .flag import FlagFetch
from .envelope import EnvelopeStuct
from .body import BodyStructureType
from .core import AString, LiteralType, NString, NoZeroUint, TaggedBase, Base, Uint, Vec1


PartType = Vec1[NoZeroUint]


class Part(TaggedBase):
    codec_data: PartType


class Header(TaggedBase):
    codec_data: PartType | None


class HeaderFields(TaggedBase):
    codec_data: tuple[PartType | None, Vec1[AString]]


class HeaderFieldsNot(TaggedBase):
    codec_data: tuple[PartType | None, Vec1[AString]]


class Text(TaggedBase):
    codec_data: PartType | None


class Mime(TaggedBase):
    codec_data: PartType


Section = Part | Header | HeaderFields | HeaderFieldsNot | Mime | Text


class Body(TaggedBase):
    codec_data: BodyStructureType


class BodyExt(TaggedBase):
    class BodyExtVal(Base):
        section: Section | None
        origin: Uint | None
        dara: NString

    codec_data: BodyStructureType


class BodyStructure(TaggedBase):
    codec_data: BodyStructureType


class Envelope(TaggedBase):
    codec_data: EnvelopeStuct


class Flags(TaggedBase):
    codec_data: Sequence[FlagFetch]


class InternalData(TaggedBase):
    codec_data: datetime


class Rfc822(TaggedBase):
    codec_data: NString


class Rfc822Header(TaggedBase):
    codec_data: NString


class Rfc822Size(TaggedBase):
    codec_data: Uint


class Rfc822Text(TaggedBase):
    codec_data: NString


class Uid(TaggedBase):
    codec_data: NoZeroUint


class Binary(TaggedBase):
    class BinaryVal(Base):
        section: Sequence[NoZeroUint]
        value: NString | LiteralType

    codec_data: BinaryVal


class BinarySize(TaggedBase):
    class BinarySizeVal(Base):
        section: Sequence[NoZeroUint]
        size: Uint

    codec_data: BinarySizeVal


MessageDataItem = (
    Body
    | BodyExt
    | BodyStructure
    | Envelope
    | Flags
    | InternalData
    | Rfc822
    | Rfc822Header
    | Rfc822Size
    | Rfc822Text
    | Uid
    | Binary
    | BinarySize
)

class Macro(TaggedBase):
    codec_data: Literal["Fast", "Full", "All"]
