# from msgspec import convert

# from imap_codec_model.thread import ThreadType
# from imap_codec_model.utils import reduce_codec_model

# c = convert(
#     cc :={
#         "codec_model": "Members",
#         "codec_data": {
#             "prefix": [1],
#             "answers": [
#                 {
#                     "codec_model": "Members",
#                     "codec_data": {
#                         "prefix": [1],
#                         "answers": [
#                             {"codec_model": "Members", "codec_data": {"prefix": [1], "answers": None}},
#                             {"codec_model": "Members", "codec_data": {"prefix": [2], "answers": None}},
#                         ],
#                     },
#                 },
#                 {"codec_model": "Members", "codec_data": {"prefix": [2], "answers": None}},
#             ],
#         },
#     },
#     ThreadType,
# )

# print(c)
# print(reduce_codec_model(cc))

# from typing import TypeVar, Annotated
# from collections.abc import Sequence
# from msgspec import Meta, Struct, convert

# T = TypeVar("T")

# Vec2 = Annotated[Sequence[T], Meta(min_length=2)]

# class A(Struct):
#     data: Vec2[int]

# print(convert({"data": [1,2]}, A))
