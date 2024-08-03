import pytest

from imap_codec_model.utils import reduce_codec_model, reshape_codec_dict, CodecDataModel


@pytest.fixture(scope="module")
def reshaped_dict() -> CodecDataModel:
    return {
        "codec_model": "Status",
        "codec_data": {
            "codec_model": "Ok",
            "tag": "a001",
            "code": {"codec_model": "UnSeen", "codec_data": 17},
            "text": "Message 17 is the first unseen message",
            "more": [
                {
                    "codec_model": "Items",
                    "codec_data": [
                        {"codec_model": "Name", "codec_data": "Apple"},
                        {"codec_model": "Name", "codec_data": "Banana"},
                    ],
                },
                {
                    "codec_model": "Item",
                    "name": "Banana",
                },
                {"age": 18},
                {
                    "codec_model": "Buffer",
                    "codec_data": "Hello, World!",
                },
            ],
        },
    }


@pytest.fixture(scope="module")
def reduced_dict():
    return {
        "Status": {
            "Ok": {
                "tag": "a001",
                "code": {"UnSeen": 17},
                "text": "Message 17 is the first unseen message",
                "more": [
                    {"Items": [{"Name": "Apple"}, {"Name": "Banana"}]},
                    {"Item": {"name": "Banana"}},
                    {"age": 18},
                    {"Buffer": "Hello, World!"},
                ],
            }
        }
    }


def test_transform(reshaped_dict, reduced_dict):
    test_reduced_dict = reduce_codec_model(reshaped_dict)
    test_reshaped_dict = reshape_codec_dict(test_reduced_dict)

    assert test_reshaped_dict == reshaped_dict
    assert test_reduced_dict == reduced_dict
    assert test_reshaped_dict == reshape_codec_dict(reduce_codec_model(reshaped_dict))
    assert test_reduced_dict == reduce_codec_model(reshape_codec_dict(reduced_dict))
