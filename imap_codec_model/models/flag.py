from typing import Literal

from .core import TaggedBase

class FlagExtension(TaggedBase, tag="Extension"):
    codec_data: str

class Keyword(TaggedBase, tag="Keyword"):
    codec_data: str

class Flag(TaggedBase):
    codec_data: (
        Literal[
            "Answered",
            "Deleted",
            "Draft",
            "Flagged",
            "Seen",
        ]
        | FlagExtension
        | Keyword
    )

FlagPerm = Flag | Literal["Asterisk"]

FlagFetch = Flag | Literal["Recent"]

class FlagNameAttribute(TaggedBase):
    codec_data: Literal["Noinferiors", "Noselect", "Marked", "Unmarked"] | FlagExtension

StoreType = Literal[
    "Replace",
    "Add",
    "Remove",
]

StoreResponse = Literal[
    "Answer",
    "Silent",
]
