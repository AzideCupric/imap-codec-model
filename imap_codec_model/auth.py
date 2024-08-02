from typing import Literal
from collections.abc import Sequence
from .core import TaggedBase, Uint

class Continue(TaggedBase):
    codec_data: Sequence[Uint]

AuthenticateData = Continue | Literal["Cancel"]

