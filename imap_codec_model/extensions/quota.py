from typing import Literal
from imap_codec_model.core import Base, StrOther, Uint


Resource = Literal["Storage", "Message", "Mailbox", "AnnotationStorage"] | StrOther


class QuotaSet(Base):
    resource: Resource
    limit: Uint

class QuotaGet(Base):
    resource: Resource
    usage: Uint
    limit: Uint
