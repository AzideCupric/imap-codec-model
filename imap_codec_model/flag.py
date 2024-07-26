from typing import Literal

from .core import Tagged

class Flag(Tagged):
    class Extension(Tagged):
        codec_data: str

    class Keyword(Tagged):
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
