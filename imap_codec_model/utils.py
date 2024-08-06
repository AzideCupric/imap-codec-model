from typing_extensions import TypedDict
from typing import TYPE_CHECKING, Any, TypeGuard, cast


class CodecDictModel(TypedDict, closed=True):
    codec_model: str
    __extra_items__: Any


class CodecDataModel(TypedDict):
    codec_model: str
    codec_data: Any


def is_codec_model_convertable(__input: Any) -> TypeGuard[dict[str, Any]]:
    """Check if the input is a dict that can be converted to `CodecDict`"""
    if not isinstance(__input, dict) or len(__input) != 1:
        return False
    key = str(next(iter(__input.keys())))

    # Check if the key is a valid identifier in PascalCase
    return key[0].isupper() and key.isidentifier()


def is_codec_anonymous_value(__input: Any) -> bool:
    """Check if the input is an anonymous value, i.e., a value with `codec_data` as the key"""
    return not (isinstance(__input, dict) and not is_codec_model_convertable(__input))


def is_codec_dict_model(__input: Any) -> TypeGuard[CodecDictModel]:
    """Check if the input is a dictionary of type `CodecDictModel`."""
    return isinstance(__input, dict) and "codec_model" in __input and "codec_data" not in __input


def is_codec_data_model(__input: Any) -> TypeGuard[CodecDataModel]:
    """Check if the input is a dictionary of type `CodecDataModel`."""
    return isinstance(__input, dict) and {"codec_model", "codec_data"} == __input.keys()


def reshape_codec_dict(__input: Any) -> dict[str, Any]:
    """Reshape the dictionary format returned by `[*]codec.decode` recursively.

    Specifically, transform an output structure like:
    ```json
    {
        "Status": {
            "Ok": {
                "tag": "a001",
                "code": {
                    "UnSeen": 17
                },
                "text": "Message 17 is the first unseen message",
            }
        }
    }
    ```
    into a structure like:
    ```json
    {
        "codec_model": "Status",
        "codec_data": {
            "codec_model": "Ok",
            "tag": "a001",
            "code": {
                "codec_model": "UnSeen",
                "codec_data": 17
            },
            "text": "Message 17 is the first unseen message"
        }
    }
    ```
    to facilitate handling the data using a `tagged union` approach.

    ## CodecDictModel
    1. `codec_model`: The key name, a PascalCase string.
    2. The key value is a dictionary with more than one key-value pair,
        where the key names do not start with an uppercase letter.

        ```json
        {
            "Aaa": {
                "bbb": 1,
                "ccc": [1, 2]
            }
        }
        ```
        is transformed into
        ```json
        {
            "codec_model": "Aaa",
            "bbb": 1,
            "ccc": [1, 2]
        }
        ```

    ## CodecDataModel
    1. `codec_model`: The key name, a PascalCase string.
    2. The key value is a basic type, list, a dictionary that does not meet the `CodecDictModel` requirements,
        or a dictionary that meets the `CodecDataModel` requirements.

        ```json
        {
            "Aaa": {
                "Bbb": 1
            }
        }
        ```
        is transformed into
        ```json
        {
            "codec_model": "Aaa",
            "codec_data": {
                "codec_model": "Bbb",
                "codec_data": 1
            }
        }
        ```

    ## Special Cases
    When the key value is a string in PascalCase, it should theoretically be a CodecModel.
    However, because its value is a basic type and can be easily confused with text, it is not specially handled.
        ```json
        {
            "Status": "Ok"
        }

        {
            "Text": "Success"
        }
        ```
    As we can see, they are strings that start with an uppercase letter, and they are not specially handled.

    ## Parameters and Return Values

    - Args:
        - codec_dict (dict[str, Any]): The dictionary output by `[*]codec.decode`.

    - Returns:
        - CodecDict: The adjusted dictionary,
            separating the structural key-value pairs into `codec_model` and `codec_data`.
    """

    def _reshape_recursive(__input: Any) -> Any:
        if is_codec_model_convertable(__input):
            k, v = next(iter(__input.items()))
            if is_codec_anonymous_value(v):
                return CodecDataModel({"codec_model": k, "codec_data": _reshape_recursive(v)})

            reshaped_value = _reshape_recursive(v)
            return CodecDictModel({"codec_model": k, **reshaped_value})
        elif isinstance(__input, dict):
            return {k: _reshape_recursive(v) for k, v in __input.items()}
        elif isinstance(__input, list | tuple):
            return [_reshape_recursive(v) for v in __input]
        else:
            return __input

    return _reshape_recursive(__input)


def reduce_codec_model(__input: Any) -> dict[str, Any]:
    """Restore the dictionary structure adjusted by `reshape_codec_dict` to its original form.

    Args:
        codec_dict (CodecDict): The adjusted dictionary.

    Returns:
        dict[str, Any]: The original dictionary.
    """

    def _reduce_recursive(__input: Any) -> Any:
        if is_codec_dict_model(__input):
            k = __input["codec_model"]
            v = __input.copy()
            if TYPE_CHECKING:
                v = cast(dict[str, Any], v)
            v.pop("codec_model")
            return {k: _reduce_recursive(v)}
        elif is_codec_data_model(__input):
            return {__input["codec_model"]: _reduce_recursive(__input["codec_data"])}
        elif isinstance(__input, dict):
            return {k: _reduce_recursive(v) for k, v in __input.items()}
        elif isinstance(__input, list | tuple):
            return [_reduce_recursive(v) for v in __input]
        else:
            return __input

    return _reduce_recursive(__input)
