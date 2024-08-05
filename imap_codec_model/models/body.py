from __future__ import annotations
from collections.abc import Sequence

from .envelope import EnvelopeStuct


from .core import IString, NString, TaggedBase, Base, Uint, Vec1

class Single(TaggedBase):
    body: Body
    extension_data: SinglePartExtensionData | None

class Multi(TaggedBase):
    bodies: Vec1[BodyStructureType]
    subtype: IString
    extension_data: MultiPartExtensionData | None

BodyStructureType = Single | Multi

class Body(Base):
    basic: BasicFields
    specific: SpecificFields


class BasicFields(Base):
    parameter_list: Sequence[tuple[IString, IString]]
    id: NString
    description: NString
    content_transfer_encoding: IString
    size: Uint

class Basic(TaggedBase):
    type: IString
    subtype: IString


class Message(TaggedBase):
    envelope: EnvelopeStuct
    body_structure: BodyStructureType
    number_of_lines: Uint


class Text(TaggedBase):
    subtype: IString
    number_of_lines: Uint


SpecificFields = Basic | Text | Message

class SinglePartExtensionData(Base):
    md5: NString
    tail: Disposition | None


class MultiPartExtensionData(Base):
    parameter_list: Sequence[tuple[IString, IString]]
    tail: Disposition | None


class Disposition(Base):
    disposition: tuple[IString, Sequence[tuple[IString, IString]]] | None
    tail: Language | None


class Language(Base):
    languages: Sequence[IString]
    tail: Location | None


class Location(Base):
    location: NString
    extensions: Sequence[BodyExtension]


class BodyExtensionNString(TaggedBase, tag="NString"):
    codec_data: NString

class BodyExtensionNumber(TaggedBase, tag="Number"):
    codec_data: Uint

class BodyExtensionList(TaggedBase, tag="List"):
    codec_data: Vec1[BodyExtension]

BodyExtension = BodyExtensionNString | BodyExtensionNumber | BodyExtensionList
