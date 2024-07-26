from typing import Annotated, Literal
from collections.abc import Sequence

from msgspec import Meta

from imap_codec_model.flag import FlagPerm
from imap_codec_model.metadata import MetadataCode
from imap_codec_model.uidplus import UidSet

from .core import Base, NoZeroUint, Tagged, Charset, StrOther

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


class BadCharset(Tagged):
    class Allowed(Base):
        allowed: Sequence[Charset]

    codec_data: Allowed


class Capability(Tagged):
    class Auth(Tagged):
        codec_data: (
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

    class Compress(Tagged):
        class Algorithm(Base):
            algorithm: Literal["Deflate"]

        codec_data: Algorithm

    class QuotaRes(Tagged):
        codec_data: Literal["Storage", "Message", "Mailbox", "AnnotationStorage"] | StrOther

    class Sort(Tagged):
        codec_data: Literal["Display",] | StrOther | None

    class Thread(Tagged):
        codec_data: (
            Literal[
                "OrderedSubject",
                "References",
            ]
            | StrOther
        )

    codec_data: tuple[
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
    ]


class PermanentFlags(Tagged):
    codec_data: Sequence[FlagPerm]


class UidNext(Tagged):
    codec_data: Annotated[int, Meta(gt=0)]


class UidValidity(Tagged):
    codec_data: Annotated[int, Meta(gt=0)]


class Unseen(Tagged):
    codec_data: Annotated[int, Meta(ge=0)]


class Referral(Tagged):
    codec_data: str


class Metadata(Tagged):
    codec_data: MetadataCode


class AppendUid(Tagged):
    class Uid(Base):
        uid_validity: NoZeroUint
        uid: NoZeroUint

    codec_data: Uid


class CopyUid(Tagged):
    class Uid(Base):
        uid_validity: NoZeroUint
        source: UidSet
        destination: UidSet

    codec_data: Uid


class CodeOther(Tagged, tag="Other"):
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

GreetingKind = Literal[
    "Ok",
    "PreAuth",
    "Bye",
]


class Greeting(Base):
    kind: GreetingKind
    code: Code | None
    text: str | None
