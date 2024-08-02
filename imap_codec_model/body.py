from __future__ import annotations
from collections.abc import Sequence

from .envelope import EnvelopeStuct


from .core import IString, NString, TaggedBase, Base, Uint, Vec1

class Single(TaggedBase):
    class SingleVal(Base):
        body: Body
        extension_data: SinglePartExtensionData | None

    codec_data: SingleVal

class Multi(TaggedBase):
    class MultiVal(Base):
        bodies: Vec1[BodyStructureType]
        subtype: IString
        extension_data: MultiPartExtensionData | None

    codec_data: MultiVal

BodyStructureType = Single | Multi

class Body(Base):
    class BodyVal(Base):
        basic: BasicFields
        specific: SpecificFields

    codec_data: BodyVal

class BasicFields(Base):
    class BasicFieldsVal(Base):
        parameter_list: Sequence[tuple[IString, IString]]
        id: NString
        description: NString
        content_transfer_encoding: IString
        size: Uint

    codec_data: BasicFieldsVal

class Basic(TaggedBase):
    class BasicVal(Base):
        type: IString
        subtype: IString

    codec_data: BasicVal

class Message(TaggedBase):
    class MessageVal(Base):
        envelope: EnvelopeStuct
        body_structure: BodyStructureType
        number_of_lines: Uint

    codec_data: MessageVal

class Text(TaggedBase):
    class TextVal(Base):
        subtype: IString
        number_of_lines: Uint

    codec_data: TextVal

SpecificFields = Basic | Text | Message

class SinglePartExtensionData(Base):
    class SinglePartExtensionDataVal(Base):
        md5: NString
        tail: Disposition | None

    codec_data: SinglePartExtensionDataVal

class MultiPartExtensionData(Base):
    class MultiPartExtensionDataVal(Base):
        parameter_list: Sequence[tuple[IString, IString]]
        tail: Disposition | None

    codec_data: MultiPartExtensionDataVal

class Disposition(Base):
    class DispositionVal(Base):
        disposition: tuple[IString, Sequence[tuple[IString, IString]]] | None
        tail: Language | None

    codec_data: DispositionVal

class Language(Base):
    class LanguageVal(Base):
        languages: Sequence[IString]
        tail: Location | None

    codec_data: LanguageVal

class Location(Base):
    class LocationVal(Base):
        location: NString
        extensions: Sequence[BodyExtension]

    codec_data: LocationVal

class BodyExtensionNString(TaggedBase, tag="NString"):
    codec_data: NString

class BodyExtensionNumber(TaggedBase, tag="Number"):
    codec_data: Uint

class BodyExtensionList(TaggedBase, tag="List"):
    codec_data: Vec1[BodyExtension]

BodyExtension = BodyExtensionNString | BodyExtensionNumber | BodyExtensionList
