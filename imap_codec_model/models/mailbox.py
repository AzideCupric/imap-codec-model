from typing import Literal
from .core import IString, StrOther, TaggedBase

Mailbox = Literal["Inbox"] | StrOther

class Token(TaggedBase):
    codec_data: str

class MailboxString(TaggedBase, tag="String"):
    codec_data: IString

ListMailbox = Token | MailboxString
