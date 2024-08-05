from typing import Any, TypeVar, overload
from typing_extensions import assert_never

import msgspec
from imap_codec import Greeting, Command, AuthenticateData, Response, IdleDone
from imap_codec import GreetingCodec, CommandCodec, AuthenticateDataCodec, ResponseCodec, IdleDoneCodec
from imap_codec import Encoded

from .models import (
    Greeting as GreetingModel,
    Command as CommandModel,
    AuthenticateData as AuthenticateDataModel,
    Response as ResponseModel,
)

from .utils import reshape_codec_dict, reduce_codec_model

T = TypeVar("T")

T_Codec = GreetingCodec | CommandCodec | AuthenticateDataCodec | ResponseCodec | IdleDoneCodec
T_Model = GreetingModel | CommandModel | AuthenticateDataModel | ResponseModel

@overload
def type_codec_decode(codec: type[GreetingCodec], data: bytes) -> tuple[bytes, GreetingModel]: ...

@overload
def type_codec_decode(codec: type[CommandCodec], data: bytes) -> tuple[bytes, CommandModel]: ...

@overload
def type_codec_decode(codec: type[AuthenticateDataCodec], data: bytes) -> tuple[bytes, AuthenticateDataModel]: ...

@overload
def type_codec_decode(codec: type[ResponseCodec], data: bytes) -> tuple[bytes, ResponseModel]: ...

@overload
def type_codec_decode(codec: type[IdleDoneCodec], data: bytes) -> tuple[bytes, IdleDone]: ...


def type_codec_decode(codec: type[T_Codec], data: bytes) -> tuple[bytes, T_Model | IdleDone]:
    remaining, struct = codec.decode(data)
    if isinstance(struct, IdleDone):
        return remaining, struct

    reshaped_dict = reshape_codec_dict(struct.as_dict())
    match struct:
        case Greeting():
            return remaining, msgspec.convert(reshaped_dict, GreetingModel)
        case Command():
            return remaining, msgspec.convert(reshaped_dict, CommandModel)
        case AuthenticateData():
            return remaining, msgspec.convert(reshaped_dict, AuthenticateDataModel)
        case Response():
            return remaining, msgspec.convert(reshaped_dict, ResponseModel)
        case _:
            assert_never(struct)

def type_codec_encode(model: T_Model) -> Encoded:
    reshaped_dict = reduce_codec_model(msgspec.to_builtins(model))

    match model:
        case GreetingModel():
            return GreetingCodec.encode(Greeting.from_dict(reshaped_dict))
        case CommandModel():
            return CommandCodec.encode(Command.from_dict(reshaped_dict))
        case value if isinstance(value, AuthenticateDataModel):
            return AuthenticateDataCodec.encode(AuthenticateData.from_dict(reshaped_dict))
        case value if isinstance(value, ResponseModel):
            return ResponseCodec.encode(Response.from_dict(reshaped_dict))
        case _:
            assert_never(model) # type: ignore

def model_dump(model: T_Model, reduce: bool = True) -> dict[str, Any]:
    model_dict = msgspec.to_builtins(model)

    return reduce_codec_model(model_dict) if reduce else model_dict
