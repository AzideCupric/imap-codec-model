import pytest
import msgspec

from imap_codec import GreetingCodec, Greeting as GreetingCodecModel

from imap_codec_model.greeting import Greeting
from imap_codec_model.utils import reshape_codec_dict, reduce_codec_model


@pytest.mark.parametrize(
    "case",
    [
        {"kind": "Ok", "code": None, "text": "Hello, World!"},
        {"kind": "PreAuth", "code": "Alert", "text": "Bye, World!"},
        {
            "kind": "Ok",
            "code": {"BadCharset": {"allowed": [{"Atom": "US-ASCII"}, {"Quoted": "UTF-8"}]}},
            "text": "(Success)",
        },
        {
            "kind": "Ok",
            "code": {"PermanentFlags": ["Asterisk", {"Flag": "Seen"}, {"Flag": {"Keyword": "we"}}]},
            "text": "(Success)",
        },
        {"kind": "Ok", "code": {"AppendUid": {"uid_validity": 1, "uid": 1}}, "text": "(Success)"},
        {
            "kind": "Ok",
            "code": {"CopyUid": {"uid_validity": 1, "source": [{"Single": 1}], "destination": [{"Range": (1, 2)}]}},
            "text": "(Success)",
        },
        {"kind": "Ok", "code": {"Other": [85, 85, 73, 68]}, "text": "(Success)"},
    ],
)
def test_greeting_parse(case):
    greeting_dict = reshape_codec_dict(case)
    greeting = msgspec.convert(greeting_dict, Greeting)

    res = reduce_codec_model(msgspec.to_builtins(greeting))
    assert GreetingCodecModel.from_dict(res) == GreetingCodecModel.from_dict(case)
    assert (
        GreetingCodec.encode(GreetingCodecModel.from_dict(res)).dump()
        == GreetingCodec.encode(GreetingCodecModel.from_dict(case)).dump()
    )
