from datetime import date
from typing import Literal
from .core import AString, Atom, TaggedBase, Uint, Vec1
from .sequence import SequenceSet as SequenceSetType


class And(TaggedBase):
    codec_data: Vec1["SearchKey"]


class SequenceSet(TaggedBase):
    codec_data: SequenceSetType


class Bcc(TaggedBase):
    codec_data: AString


class Before(TaggedBase):
    codec_data: date


class Cc(TaggedBase):
    codec_data: AString


class From(TaggedBase):
    codec_data: AString


class Header(TaggedBase):
    codec_data: tuple[AString, AString]


class Keyword(TaggedBase):
    codec_data: Atom


class Larger(TaggedBase):
    codec_data: int


class Not(TaggedBase):
    codec_data: "SearchKey"


class On(TaggedBase):
    codec_data: date


class Or(TaggedBase):
    codec_data: tuple["SearchKey", "SearchKey"]


class SentBefore(TaggedBase):
    codec_data: date


class SentOn(TaggedBase):
    codec_data: date


class SendSince(TaggedBase):
    codec_data: date


class Since(TaggedBase):
    codec_data: date


class Smaller(TaggedBase):
    codec_data: Uint


class Subject(TaggedBase):
    codec_data: AString


class Text(TaggedBase):
    codec_data: AString


class To(TaggedBase):
    codec_data: AString


class Uid(TaggedBase):
    codec_data: SequenceSet


class UnKeyword(TaggedBase):
    codec_data: Atom


SearchKey = (
    Literal[
        "All",
        "Answered",
        "Deleted",
        "Draft",
        "Flagged",
        "New",
        "Old",
        "Recent",
        "Seen",
        "Unanswered",
        "Undeleted",
        "Undraft",
        "Unseen",
    ]
    | And
    | Bcc
    | Before
    | Cc
    | From
    | Header
    | Keyword
    | Larger
    | Not
    | On
    | Or
    | SentBefore
    | SentOn
    | SendSince
    | Since
    | Smaller
    | Subject
    | Text
    | To
    | Uid
    | UnKeyword
)
