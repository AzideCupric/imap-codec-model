from typing import Literal

from .core import TaggedBase

class Flag(TaggedBase):
    class Extension(TaggedBase):
        codec_data: str

    class Keyword(TaggedBase):
        codec_data: str

    codec_data: (
        Literal[
            "Answered",
            "Deleted",
            "Draft",
            "Flagged",
            "Seen",
        ]
        | Extension
        | Keyword
    )

FlagPerm = Flag | Literal["Asterisk"]

FlagFetch = Flag | Literal["Recent"]

class FlagNameAttribute(TaggedBase):
    class Extension(TaggedBase):
        codec_data: str

    codec_data: Literal["Noinferiors", "Noselect", "Marked", "Unmarked"] | Extension

StoreType = Literal[
    "Replace",
    "Add",
    "Remove",
]

StoreResponse = Literal[
    "Answer",
    "Silent",
]
