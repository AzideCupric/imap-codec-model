import json
from imap_codec import CommandCodec
from imap_codec_model.validate import type_codec_decode, type_codec_encode, model_dump


def test_dencode():
    _, a = type_codec_decode(CommandCodec, b"ABCD UID FETCH 1,2:* (BODY.PEEK[1.2.3.4.MIME]<42.1337>)\r\n")

    _, b = CommandCodec.decode(b"ABCD UID FETCH 1,2:* (BODY.PEEK[1.2.3.4.MIME]<42.1337>)\r\n")

    assert type_codec_encode(a).dump() == CommandCodec.encode(b).dump()

    # FIXME: in model, range will convert to a tuple, but the original is a list.
    # in fact, they are equal and tuple is more excatly

    # assert model_dump(a) == b.as_dict()
    assert json.loads(json.dumps(model_dump(a))) == json.loads(json.dumps(b.as_dict()))
