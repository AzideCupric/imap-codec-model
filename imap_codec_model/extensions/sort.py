from typing import Literal
from imap_codec_model.core import Base

SortKey = Literal[
    "Arrival",
    "Cc",
    "Date",
    "From",
    "Size",
    "Subject",
    "To",
    "DisplayFrom",
    "DisplayTo",
    ]

class SortCriterion(Base):
    reverse: bool
    key: SortKey
