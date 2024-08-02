from typing import Literal
from imap_codec_model.code import Code
from imap_codec_model.core import Base, TaggedBase

StatusKind = Literal["Ok", "No", "Bad"]

class StatusBody(Base):
    kind: StatusKind
    code: Code | None
    text: str

class Untagged(TaggedBase):
    codec_data: StatusBody

class Tagged(TaggedBase):
    class TaggedVal(Base):
        tag: str
        body: StatusBody

    codec_data: TaggedVal

class Bye(TaggedBase):
    class ByeVal(Base):
        code: Code | None
        text: str

    codec_data: ByeVal

Status = Untagged | Tagged | Bye
