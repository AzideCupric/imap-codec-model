from typing import Literal
from collections.abc import Sequence

from imap_codec_model.compress import CompressionAlgorithm

from .flag import FlagPerm
from .metadata import MetadataCode
from .uidplus import UidSet
from .core import Base, NoZeroUint, TaggedBase, Charset, StrOther, Vec1

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
    class Allowed(Base):
        allowed: Sequence[Charset]

    codec_data: Allowed

AuthMechanism = (
    Literal[
        "Plain",
        "Login",
        "OAuthBearer",
        "XOAuth2",
        "ScramSha1",
        "ScramSha1Plus",
        "ScramSha256",
        "ScramSha256Plus",
        "ScramSha3_512",
        "ScramSha3_512Plus",
    ]
    | StrOther
)

class Auth(TaggedBase):
    codec_data: AuthMechanism


class Compress(TaggedBase):
    class Algorithm(Base):
        algorithm: CompressionAlgorithm

    codec_data: Algorithm

Resource = Literal["Storage", "Message", "Mailbox", "AnnotationStorage"]

class QuotaRes(TaggedBase):
    codec_data: Resource | StrOther


class Sort(TaggedBase):
    codec_data: Literal["Display",] | StrOther | None


class Thread(TaggedBase):
    codec_data: (
        Literal[
            "OrderedSubject",
            "References",
        ]
        | StrOther
    )


CapabilityType = (
    Literal[
        "Imap4Rev1",
        "LoginDisabled",
        "StartTls",
        "Idle",
        "MailboxReferrals",
        "LoginReferrals",
        "SaslTr",
        "Enable",
        "Quota",
        "QuotaSet",
        "LiteralPlus",
        "LiteralMinus",
        "Move",
        "Id",
        "Unselect",
        "Metadata",
        "MetadataServer",
        "Binary",
        "UidPlus",
    ]
    | Auth
    | Compress
    | QuotaRes
    | Sort
    | Thread
    | StrOther
)


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
    class Uid(Base):
        uid_validity: NoZeroUint
        uid: NoZeroUint

    codec_data: Uid


class CopyUid(TaggedBase):
    class Uid(Base):
        uid_validity: NoZeroUint
        source: UidSet
        destination: UidSet

    codec_data: Uid


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
