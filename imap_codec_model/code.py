from typing import Literal
from collections.abc import Sequence

from .capability import CapabilityType

from .flag import FlagPerm
from .extensions.metadata import MetadataCode
from .extensions.uidplus import UidSet
from .core import NoZeroUint, TaggedBase, Charset, Vec1

CodeLiteral = Literal[
    "Alert",
    "Parse",
    "ReadOnly",
    "ReadWrite",
    "TryCreate",
    "CompressionActive",
    "OverQuota",
    "TooBig",
    "UnknownCte",
    "UidNotSticky",
]


class BadCharset(TaggedBase):
    allowed: Sequence[Charset]


class Capability(TaggedBase):
    codec_data: Vec1[CapabilityType]


class PermanentFlags(TaggedBase):
    codec_data: Sequence[FlagPerm]


class UidNext(TaggedBase):
    codec_data: NoZeroUint


class UidValidity(TaggedBase):
    codec_data: NoZeroUint


class Unseen(TaggedBase):
    codec_data: NoZeroUint


class Referral(TaggedBase):
    codec_data: str


class Metadata(TaggedBase):
    codec_data: MetadataCode


class AppendUid(TaggedBase):
    uid_validity: NoZeroUint
    uid: NoZeroUint


class CopyUid(TaggedBase):
    uid_validity: NoZeroUint
    source: UidSet
    destination: UidSet


class CodeOther(TaggedBase, tag="Other"):
    codec_data: Sequence[int]


Code = (
    CodeLiteral
    | BadCharset
    | Capability
    | PermanentFlags
    | UidNext
    | UidValidity
    | Unseen
    | Referral
    | Metadata
    | AppendUid
    | CopyUid
    | CodeOther
)
