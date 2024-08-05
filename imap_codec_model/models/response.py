from collections.abc import Sequence
from typing import Literal

from .enable import CapabilityEnable
from .fetch import MessageDataItem
from .extensions.metadata import MetadataResponse
from .extensions.quota import QuotaGet
from .status import StatusDataItem
from .mailbox import Mailbox
from .flag import Flag, FlagNameAttribute
from .core import AString, Base, IString, NString, NoZeroUint, QuotedChar, TaggedBase, Uint, Vec1
from .code import Capability, Code
from .extensions.thread import ThreadType


class List(TaggedBase):
    items: Sequence[FlagNameAttribute]
    delimiter: QuotedChar | None
    mailbox: Mailbox



class Lsub(TaggedBase):
    items: Sequence[FlagNameAttribute]
    delimiter: QuotedChar | None
    mailbox: Mailbox



# 与Data同级的Status类冲突，改为DataStatus
class DataStatus(TaggedBase, tag="Status"):
    mailbox: Mailbox
    items: Sequence[StatusDataItem]


class Search(TaggedBase):
    codec_data: Sequence[NoZeroUint]


class Sort(TaggedBase):
    codec_data: Sequence[NoZeroUint]


class Thread(TaggedBase):
    codec_data: Sequence[ThreadType]


class Flags(TaggedBase):
    codec_data: Sequence[Flag]


class Exists(TaggedBase):
    codec_data: Uint


class Recent(TaggedBase):
    codec_data: Uint


class Expunge(TaggedBase):
    codec_data: NoZeroUint


class Fetch(TaggedBase):
    seq: NoZeroUint
    items: Vec1[MessageDataItem]



class Enable(TaggedBase):
    capabilities: Sequence[CapabilityEnable]


class Quota(TaggedBase):
    root: AString
    quotas: Vec1[QuotaGet]


class QuotaRoot(TaggedBase):
    mailbox: Mailbox
    roots: Sequence[AString]



class Id(TaggedBase):
    parameters: Sequence[tuple[IString, NString]] | None



class Metadata(TaggedBase):
    mailbox: Mailbox
    items: MetadataResponse


DataType = (
    Capability
    | List
    | Lsub
    | DataStatus
    | Search
    | Sort
    | Thread
    | Flags
    | Exists
    | Recent
    | Expunge
    | Fetch
    | Enable
    | Quota
    | QuotaRoot
    | Id
    | Metadata
)


class Data(TaggedBase):
    codec_data: DataType

StatusKind = Literal["Ok", "No", "Bad"]

class StatusBody(Base):
    kind: StatusKind
    code: Code | None
    text: str

class Untagged(TaggedBase):
    kind: StatusKind
    code: Code | None
    text: str

class Tagged(TaggedBase):
    tag: str
    body: StatusBody

class Bye(TaggedBase):
    code: Code | None
    text: str

class Status(TaggedBase):
    codec_data: Untagged | Tagged | Bye

class Basic(TaggedBase):
    code: Code | None
    text: str


class Base64(TaggedBase):
    codec_data: Sequence[Uint]

class CommandContinuationRequest(TaggedBase):
    codec_data: Basic | Base64

Response = Data | Status | CommandContinuationRequest
