from typing import Literal

from .core import Base
from .code import Code


GreetingKind = Literal[
    "Ok",
    "PreAuth",
    "Bye",
]


class Greeting(Base):
    kind: GreetingKind
    code: Code | None
    text: str | None
