import pytest
import requests
import json
import conftest
import cerberus

@pytest.mark.parametrize("url, status",[
    ("https://dog.ceo/dog-api/", 200),
    ("https://dog.ceo/api/breeds/list/all", 200),
    ("https://dog.ceo/dog-api/documentation/random", 200),
    ("https://dog.ceo/dog-api/documentation/breed", 200),
    ("https://dog.ceo/dog-api/documentation/sub-breed", 200),
    ("https://dog.ceo/dog-api/breeds-list", 200)
])
def test_status_1(url, status):
    return conftest.test_url_status(url, status)

def test_status_2(base_url, status):
    return conftest.test_url_status("https://dog.ceo/dog-api/1231231", 404)

@pytest.mark.parametrize("url, schema",[
    ("https://dog.ceo/api/breed/hound/list", {
        "message": {"type": "list"},
        "status": {"type": "string"}
    }),
    ("https://dog.ceo/api/breed/hound/images", {
        "message": {"type": "list"},
        "status": {"type": "string"}
    }),
    ("https://dog.ceo/api/breeds/image/random", {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }),
    ("https://dog.ceo/api/breeds/list/all", {
        "message": {"type": "dict"},
        "status": {"type": "string"}
    }),
])
def test_scheme(url, schema):
    res = requests.get(url)

    v = cerberus.Validator()

    assert v.validate(res.json(), schema)

def test_json_1():
    res = requests.get("https://dog.ceo/api/breed/hound/list")

    expected_json = {
        "message": [
            "afghan",
            "basset",
            "blood",
            "english",
            "ibizan",
            "plott",
            "walker"
        ],
        "status": "success"
    }

    assert res.json() == expected_json

def test_json_2():
    res = requests.get("https://dog.ceo/api/breed/hound/images")

    with open("data_1.json") as f:
        expected_json = json.load(f)

    assert res.json() == expected_json
