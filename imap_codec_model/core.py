from typing import Annotated

from msgspec import Struct, Meta

Base = Struct
"""为非CodecModel的基类"""


class Tagged(Struct, tag_field="codec_model", tag=lambda name: name.split(".")[-1]):
    """为CodecModel的基类，tag_field指定了tag字段的名称为codec_model: <class name>，
    继承时不需要显式指定tag_field和codec_model字段
    """
    pass


class Atom(Tagged):
    codec_data: str


class Quoted(Tagged):
    codec_data: str


Charset = Atom | Quoted

NoZeroUint = Annotated[int, Meta(gt=0)]
"""大于0的整数"""

class StrOther(Tagged, tag="Other"):
    codec_data: str
