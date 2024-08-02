from collections.abc import Sequence
from typing import Literal
from datetime import datetime

from msgspec import field

from imap_codec_model.compress import CompressionAlgorithm
from imap_codec_model.extensions.enable import CapabilityEnable
from imap_codec_model.extensions.quota import QuotaSet
from imap_codec_model.fetch import Macro, MessageDataItem
from imap_codec_model.flag import Flag, StoreResponse, StoreType
from imap_codec_model.mailbox import ListMailbox, Mailbox
from imap_codec_model.metadata import EntryValue, GetMetadataOption
from imap_codec_model.search import SearchKey
from imap_codec_model.sequence import SequenceSet
from imap_codec_model.sort import SortCriterion
from imap_codec_model.status import StatusDataItemName
from imap_codec_model.thread import ThreadingAlgorithm

from .code import AuthMechanism
from .core import AString, Charset, IString, LiteralType, NString, TaggedBase, Base, Uint, Vec1


class Authenticate(TaggedBase):
    class AuthenticateVal(Base):
        mechanism: AuthMechanism
        initial_response: Sequence[Uint] | None

    codec_data: AuthenticateVal


class Login(TaggedBase):
    class LoginVal(Base):
        username: AString
        password: AString

    codec_data: LoginVal


class MailboxStruct(Base):
    mailbox: Mailbox


class Select(TaggedBase):
    codec_data: MailboxStruct


class Examine(TaggedBase):
    codec_data: MailboxStruct


class Create(TaggedBase):
    codec_data: MailboxStruct


class Delete(TaggedBase):
    codec_data: MailboxStruct


class Rename(TaggedBase):
    class RenameVal(Base):
        from_: Mailbox = field(name="from")
        to: Mailbox

    codec_data: RenameVal


class Subscribe(TaggedBase):
    codec_data: MailboxStruct


class Unsubscribe(TaggedBase):
    codec_data: MailboxStruct


class List(TaggedBase):
    class ListVal(Base):
        reference: Mailbox
        mailbox_wildcard: ListMailbox

    codec_data: ListVal


class Lsub(TaggedBase):
    class LsubVal(Base):
        reference: Mailbox
        mailbox_wildcard: ListMailbox

    codec_data: LsubVal


class Status(TaggedBase):
    class StatusVal(Base):
        mailbox: Mailbox
        items: Sequence[StatusDataItemName]

    codec_data: StatusVal


class Literal_(TaggedBase, tag="Literal"):
    codec_data: LiteralType


class Literal8(TaggedBase):
    codec_data: LiteralType


class Append(TaggedBase):
    class AppendVal(Base):
        mailbox: Mailbox
        flags: Sequence[Flag]
        date: datetime | None
        message: Literal_ | Literal8 | None

    codec_data: AppendVal


class ExpungeUid(TaggedBase):
    class ExpungeUidVal(Base):
        sequence_set: SequenceSet

    codec_data: ExpungeUidVal


class Search(TaggedBase):
    class SearchVal(Base):
        charset: Charset | None
        criteria: Vec1[SearchKey]
        uid: bool

    codec_data: SearchVal


class Sort(TaggedBase):
    class SortVal(Base):
        sort_criteria: Vec1[SortCriterion]
        charset: Charset
        search_criteria: Vec1[SearchKey]
        uid: bool

    codec_data: SortVal


class Thread(TaggedBase):
    class ThreadVal(Base):
        algorithm: ThreadingAlgorithm
        charset: Charset
        search_criteria: Vec1[SearchKey]
        uid: bool

    codec_data: ThreadVal


class Fetch(TaggedBase):
    class FetchVal(Base):
        sequence_set: SequenceSet
        macro_or_item_names: Macro | Sequence[MessageDataItem]
        uid: bool

    codec_data: FetchVal


class Store(TaggedBase):
    class StoreVal(Base):
        sequence_set: SequenceSet
        kind: StoreType
        response: StoreResponse
        flags: Sequence[Flag]
        uid: bool

    codec_data: StoreVal


class Copy(TaggedBase):
    class CopyVal(Base):
        sequence_set: SequenceSet
        mailbox: Mailbox
        uid: bool

    codec_data: CopyVal


class Enable(TaggedBase):
    class EnableVal(Base):
        capabilities: Vec1[CapabilityEnable]

    codec_data: EnableVal


class Compress(TaggedBase):
    class CompressVal(Base):
        algorithm: CompressionAlgorithm

    codec_data: CompressVal


class GetQuota(TaggedBase):
    class GetQuotaVal(Base):
        root: AString

    codec_data: GetQuotaVal


class GetQuotaRoot(TaggedBase):
    class GetQuotaRootVal(Base):
        mailbox: Mailbox

    codec_data: GetQuotaRootVal


class SetQuota(TaggedBase):
    class SetQuotaVal(Base):
        root: AString
        quotas: Sequence[QuotaSet]

    codec_data: SetQuotaVal


class Move(TaggedBase):
    class MoveVal(Base):
        sequence_set: SequenceSet
        mailbox: Mailbox
        uid: bool

    codec_data: MoveVal


class Id(TaggedBase):
    class IdVal(Base):
        parameters: Sequence[tuple[IString, NString]] | None

    codec_data: IdVal


class SetMetadata(TaggedBase):
    class SetMetadataVal(Base):
        mailbox: Mailbox
        entry_values: Vec1[EntryValue]

    codec_data: SetMetadataVal


class GetMetadata(TaggedBase):
    class GetMetadataVal(Base):
        options: Sequence[GetMetadataOption]
        mailbox: Mailbox
        entrys: Vec1[AString]

    codec_data: GetMetadataVal


CommandBody = (
    Literal[
        "Capability",
        "Noop",
        "Logout",
        "StartTls",
        # "Authenticate", # has structure
        # "Login", # has structure
        # "Select", # has structure
        "Unselect",
        # "Examine", # has structure
        # "Create", # has structure
        # "Delete", # has structure
        # "Rename", # has structure
        # "Subscribe", # has structure
        # "Unsubscribe", # has structure
        # "List", # has structure
        # "Lsub", # has structure
        # "Status", # has structure
        # "Append", # has structure
        "Check",
        "Close",
        "Expunge",
        # "ExpungeUid", # has structure
        # "Search", # has structure
        # "Sort", # has structure
        # "Thread", # has structure
        # "Fetch", # has structure
        # "Store", # has structure
        # "Copy", # has structure
        "Idle",
        # "Enable", # has structure
        # "Compress", # has structure
        # "GetQuota", # has structure
        # "GetQuotaRoot", # has structure
        # "SetQuota", # has structure
        # "Move", # has structure
        # "Id", # has structure
        # "SetMetadata", # has structure
        # "GetMetadata", # has structure
    ]
    | Authenticate
    | Login
    | Select
    | Examine
    | Create
    | Delete
    | Rename
    | Subscribe
    | Unsubscribe
    | List
    | Lsub
    | Status
    | Append
    | ExpungeUid
    | Search
    | Sort
    | Thread
    | Fetch
    | Store
    | Copy
    | Enable
    | Compress
    | GetQuota
    | GetQuotaRoot
    | SetQuota
    | Move
    | Id
    | SetMetadata
    | GetMetadata
)


class Command(Base):
    tag: str
    body: CommandBody
