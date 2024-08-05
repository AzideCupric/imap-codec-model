from typing import Literal
from collections.abc import Sequence
from .core import StrOther, TaggedBase, Uint

class Continue(TaggedBase):
    codec_data: Sequence[Uint]

AuthenticateData = Continue | Literal["Cancel"]

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
