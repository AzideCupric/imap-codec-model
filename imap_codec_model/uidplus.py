from typing import Annotated
from collections.abc import Sequence

from msgspec import Meta
from imap_codec_model.core import Tagged


class Single(Tagged):
    codec_data: Annotated[int, Meta(gt=0)]

class Range(Tagged):
    codec_data: tuple[Annotated[int, Meta(gt=0)], Annotated[int, Meta(gt=0)]]


UidElement = Single | Range

UidSet = Sequence[UidElement]
