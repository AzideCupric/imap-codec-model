from collections.abc import Sequence
from typing import Literal
from datetime import datetime

from msgspec import field

from .binary import LiteralOrLiteral8
from .extensions.compress import CompressionAlgorithm
from .extensions.enable import CapabilityEnable
from .extensions.quota import QuotaSet
from .fetch import MacroOrMessageDataItemNames
from .flag import Flag, StoreResponse, StoreType
from .mailbox import ListMailbox, Mailbox
from .extensions.metadata import EntryValue, GetMetadataOption
from .search import SearchKey
from .sequence import SequenceSet
from .extensions.sort import SortCriterion
from .status import StatusDataItemName
from .extensions.thread import ThreadingAlgorithm

from .auth import AuthMechanism
from .core import AString, Charset, IString, NString, TaggedBase, Base, Uint, Vec1


class Authenticate(TaggedBase):
    mechanism: AuthMechanism
    initial_response: Sequence[Uint] | None


class Login(TaggedBase):
    username: AString
    password: AString


class Select(TaggedBase):
    mailbox: Mailbox


class Examine(TaggedBase):
    mailbox: Mailbox


class Create(TaggedBase):
    mailbox: Mailbox


class Delete(TaggedBase):
    mailbox: Mailbox


class Rename(TaggedBase):
    from_: Mailbox = field(name="from")
    to: Mailbox


class Subscribe(TaggedBase):
    mailbox: Mailbox


class Unsubscribe(TaggedBase):
    mailbox: Mailbox


class List(TaggedBase):
    reference: Mailbox
    mailbox_wildcard: ListMailbox



class Lsub(TaggedBase):
    reference: Mailbox
    mailbox_wildcard: ListMailbox



class Status(TaggedBase):
    mailbox: Mailbox
    items: Sequence[StatusDataItemName]



class Append(TaggedBase):
    mailbox: Mailbox
    flags: Sequence[Flag]
    date: datetime | None
    message: LiteralOrLiteral8



class ExpungeUid(TaggedBase):
    sequence_set: SequenceSet



class Search(TaggedBase):
    charset: Charset | None
    criteria: Vec1[SearchKey]
    uid: bool


class Sort(TaggedBase):
    sort_criteria: Vec1[SortCriterion]
    charset: Charset
    search_criteria: Vec1[SearchKey]
    uid: bool



class Thread(TaggedBase):
    algorithm: ThreadingAlgorithm
    charset: Charset
    search_criteria: Vec1[SearchKey]
    uid: bool



class Fetch(TaggedBase):
    sequence_set: SequenceSet
    macro_or_item_names: MacroOrMessageDataItemNames
    uid: bool


class Store(TaggedBase):
    sequence_set: SequenceSet
    kind: StoreType
    response: StoreResponse
    flags: Sequence[Flag]
    uid: bool



class Copy(TaggedBase):
    sequence_set: SequenceSet
    mailbox: Mailbox
    uid: bool



class Enable(TaggedBase):
    capabilities: Vec1[CapabilityEnable]



class Compress(TaggedBase):
    algorithm: CompressionAlgorithm



class GetQuota(TaggedBase):
    root: AString


class GetQuotaRoot(TaggedBase):
    mailbox: Mailbox



class SetQuota(TaggedBase):
    root: AString
    quotas: Sequence[QuotaSet]



class Move(TaggedBase):
    sequence_set: SequenceSet
    mailbox: Mailbox
    uid: bool



class Id(TaggedBase):
    parameters: Sequence[tuple[IString, NString]] | None



class SetMetadata(TaggedBase):
    mailbox: Mailbox
    entry_values: Vec1[EntryValue]



class GetMetadata(TaggedBase):
    options: Sequence[GetMetadataOption]
    mailbox: Mailbox
    entrys: Vec1[AString]



CommandBody = (
    Literal[
        "Capability",
        "Noop",
        "Logout",
        "StartTls",
        "Unselect",
        "Check",
        "Close",
        "Expunge",
        "Idle",
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
