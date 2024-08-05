from typing import Literal
from ..core import Base, StrOther, Uint


Resource = Literal["Storage", "Message", "Mailbox", "AnnotationStorage"] | StrOther


class QuotaSet(Base):
    resource: Resource
    limit: Uint

class QuotaGet(Base):
    resource: Resource
    usage: Uint
    limit: Uint
