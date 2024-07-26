from typing import Any, TypedDict, TypeGuard


class CodecDict(TypedDict):
    codec_model: str
    codec_data: Any


def is_codec_model(__input: Any) -> TypeGuard[dict[str, Any]]:
    """判断输入是否为符合可转换为`CodecDict`的dict"""
    if not isinstance(__input, dict) or len(__input) != 1:
        return False
    key = str(next(iter(__input.keys())))

    # 判断是否为`PascaleCase`的合法标识符字符串
    return key[0].isupper() and key.isidentifier()


def is_codec_dict(__input: Any) -> TypeGuard[CodecDict]:
    """判断输入是否为符合`CodecDict`的对象"""
    return isinstance(__input, dict) and __input.keys() == {"codec_model", "codec_data"}


def reshape_codec_dict(codec_dict: dict[str, Any]) -> dict[str, Any]:
    """调整*codec.decode所得到的字典格式，使用递归实现

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
            "codec_data": {
                "tag": "a001",
                "code": {
                    "codec_model": "UnSeen",
                    "codec_data": 17
                },
                "text": "Message 17 is the first unseen message"
            }
        }
    }
    ```
    的字典结构，以便后续使用`tagged union`的方式处理数据。

    Args:
        codec_dict (dict[str, Any]): *codec.decode所输出的字典

    Returns:
        CodecDict: 调整后的字典，将原字典中的结构键值对分离为`codec_model`和`codec_data`
    """

    def _reshape_recursively(__value: Any):
        match __value:
            case cd if is_codec_model(cd):
                k, v = next(iter(cd.items()))
                return CodecDict(codec_model=k, codec_data=_reshape_recursively(v))
            case list():
                return [_reshape_recursively(item) for item in __value]
            case dict():
                return {key: _reshape_recursively(value) for key, value in __value.items()}
            case v:
                return v
    return _reshape_recursively(codec_dict) # type: ignore


def reduce_codec_model(codec_model: dict[str, Any]) -> dict[str, Any]:
    """将`reshape_codec_dict`调整后的字典结构恢复为原始字典结构

    Args:
        codec_dict (CodecDict): 调整后的字典

    Returns:
        dict[str, Any]: 原始字典
    """

    def _reduce_recursively(__value: Any):
        match __value:
            case cd if is_codec_dict(cd):
                k, v = cd["codec_model"], cd["codec_data"]
                return {k: _reduce_recursively(v)}
            case list():
                return [_reduce_recursively(item) for item in __value]
            case dict():
                return {k: _reduce_recursively(v) for k, v in __value.items()}
            case v:
                return v

    return _reduce_recursively(codec_model) # type: ignore
