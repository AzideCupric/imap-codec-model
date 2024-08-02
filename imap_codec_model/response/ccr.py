"""Command continuation request responses"""
from collections.abc import Sequence
from imap_codec_model.core import TaggedBase, Base, Uint
from imap_codec_model.code import Code

class Basic(TaggedBase):
    class BasicVal(Base):
        code: Code | None
        text: str

    codec_data: BasicVal

class Base64(TaggedBase):
    codec_data: Sequence[Uint]

CommandContinuationRequest = Basic | Base64
