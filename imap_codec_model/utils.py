from typing import TYPE_CHECKING, Any, TypeGuard, cast
from typing_extensions import TypedDict

class CodecDictModel(TypedDict, closed=True):
    codec_model: str
    __extra_items__: Any

class CodecDataModel(TypedDict):
    codec_model: str
    codec_data: Any

def is_codec_model_convertable(__input: Any) -> TypeGuard[dict[str, Any]]:
    """判断输入是否为符合可转换为`CodecDict`的dict"""
    if not isinstance(__input, dict) or len(__input) != 1:
        return False
    key = str(next(iter(__input.keys())))

    # 判断是否为`PascaleCase`的合法标识符字符串
    return key[0].isupper() and key.isidentifier()

def is_codec_anonymous_value(__input: Any) -> bool:
    """判断输入是否为匿名值，即使用`codec_data`作为键的值"""
    return not (isinstance(__input, dict) and not is_codec_model_convertable(__input))

def is_codec_dict_model(__input: Any) -> TypeGuard[CodecDictModel]:
    """判断输入是否为`CodecDictModel`的字典"""
    return isinstance(__input, dict) and "codec_model" in __input and "codec_data" not in __input

def is_codec_data_model(__input: Any) -> TypeGuard[CodecDataModel]:
    """判断输入是否为`CodecDataModel`的字典"""
    return isinstance(__input, dict) and {"codec_model", "codec_data"} == __input.keys()

def reshape_codec_dict(__input: Any) -> dict[str, Any]:
    """调整[*]codec.decode所得到的字典格式，使用递归实现

    即，将形如
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
    的输出结构转换为
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
    的字典结构，以便后续使用`tagged union`的方式处理数据。

    ##　CodecDictModel
    1. `codec_model`：键名，为`PascalCase`的字符串
    2. 键值为字典，且长度大于1，键名不以大写字母开头

        ```json
        {
            "Aaa": {
                "bbb": 1,
                "ccc": [1, 2]
            }
        }
        ```
        转换为
        ```json
        {
            "codec_model": "Aaa",
            "bbb": 1,
            "ccc": [1, 2]
        }
        ```

    ## CodecDataModel
    1. `codec_model`：键名，为`PascalCase`的字符串
    2. 键值为基本类型、列表、不符合`CodecDictModel`要求的字典、符合`CodecDataModel`要求的字典

        ```json
        {
            "Aaa": {
                "Bbb": 1
            }
        }
        ```
        转换为
        ```json
        {
            "codec_model": "Aaa",
            "codec_data": {
                "codec_model": "Bbb",
                "codec_data": 1
            }
        }
        ```

    ## 特例
    当键值为`PascalCase`的字符串时，理论上应该是一个CodecModel，但是由于其值为基本类型，容易和text混淆，因此不特别处理。
        ```json
        {
            "Status": "Ok"
        }

        {
            "Text": "Success"
        }
        ```
    可见他们都是以大写字母开头的字符串，不特别处理。

    ## 参数与返回值

    - Args:
        - codec_dict (dict[str, Any]): [*]codec.decode所输出的字典

    - Returns:
        - CodecDict: 调整后的字典，将原字典中的结构键值对分离为`codec_model`和`codec_data`
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
    """将`reshape_codec_dict`调整后的字典结构恢复为原始字典结构

    Args:
        codec_dict (CodecDict): 调整后的字典

    Returns:
        dict[str, Any]: 原始字典
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
