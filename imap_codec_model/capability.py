from typing import Literal

from .extensions.thread import ThreadingAlgorithm

from .extensions.quota import Resource

from .auth import AuthMechanism
from .extensions.compress import CompressionAlgorithm
from .core import StrOther, TaggedBase


class Auth(TaggedBase):
    codec_data: AuthMechanism


class Compress(TaggedBase):
    algorithm: CompressionAlgorithm

class QuotaRes(TaggedBase):
    codec_data: Resource | StrOther


class Sort(TaggedBase):
    codec_data: Literal["Display",] | StrOther | None


class Thread(TaggedBase):
    codec_data: ThreadingAlgorithm


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
