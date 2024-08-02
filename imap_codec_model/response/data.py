from collections.abc import Sequence

from imap_codec_model.enable import CapabilityEnable
from imap_codec_model.fetch import MessageDataItem
from imap_codec_model.metadata import MetadataResponse
from imap_codec_model.status import StatusDataItem
from imap_codec_model.mailbox import Mailbox
from imap_codec_model.flag import Flag, FlagNameAttribute
from imap_codec_model.core import AString, Base, IString, NString, NoZeroUint, QuotedChar, TaggedBase, Uint, Vec1
from imap_codec_model.code import Capability, Resource
from imap_codec_model.thread import ThreadType


class List(TaggedBase):
    class ListVal(Base):
        items: Sequence[FlagNameAttribute]
        delimiter: QuotedChar | None
        mailbox: Mailbox

    codec_data: ListVal


class Lsub(TaggedBase):
    class LsubVal(Base):
        items: Sequence[FlagNameAttribute]
        delimiter: QuotedChar | None
        mailbox: Mailbox

    codec_data: LsubVal


# 与Data同级的Status类冲突，改为DataStatus
class Status(TaggedBase):
    """Data下属的Status，而非Data同级的Status"""

    class DataStatusVal(Base):
        mailbox: Mailbox
        items: Sequence[StatusDataItem]

    codec_data: DataStatusVal


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
    class FetchVal(Base):
        seq: NoZeroUint
        items: Vec1[MessageDataItem]

    codec_data: FetchVal


class Enable(TaggedBase):
    class EnableVal(Base):
        capabilities: Sequence[CapabilityEnable]

    codec_data: EnableVal


class QuotaGet(Base):
    resource: Resource
    usage: Uint
    limit: Uint


class Quota(TaggedBase):
    class QuotaVal(Base):
        root: AString
        quotas: Vec1[QuotaGet]

    codec_data: QuotaVal


class QuotaRoot(TaggedBase):
    class QuotaRootVal(Base):
        mailbox: Mailbox
        roots: Sequence[AString]

    codec_data: QuotaRootVal


class Id(TaggedBase):
    class IdVal(Base):
        parameters: Sequence[tuple[IString, NString]] | None

    codec_data: IdVal


class Metadata(TaggedBase):
    class MetadataVal(Base):
        mailbox: Mailbox
        items: MetadataResponse


DataType = (
    Capability
    | List
    | Lsub
    | Status
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
