import pytest
import requests
import json
import conftest
import cerberus


@pytest.mark.parametrize("url, status", [
    ("https://jsonplaceholder.typicode.com/posts/1/comments", 200),
    ("https://jsonplaceholder.typicode.com/albums/1/photos", 200),
    ("https://jsonplaceholder.typicode.com/users/1/albums", 200),
    ("https://jsonplaceholder.typicode.com/users/1/todos", 200),
    ("https://jsonplaceholder.typicode.com/users/1/posts", 200)
])
def test_status_1(url, status):
    return conftest.test_url_status(url, status)


def test_status_2(base_url, status):
    return conftest.test_url_status("https://jsonplaceholder.typicode.com/posts/1/comments123123sad", 404)


@pytest.mark.parametrize("url, schema", [
    ("https://jsonplaceholder.typicode.com/posts", {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    }),
    ("https://jsonplaceholder.typicode.com/albums/1/photos", {
        "albumId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "url": {"type": "string"},
        "thumbnailUrl": {"type": "string"}
    }),
    ("https://jsonplaceholder.typicode.com/users", {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "address": {
            "type": "dict",
            "schema": {
                "street": {"type": "string"},
                "suite": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"},
                "geo": {
                    "type": "dict",
                    "schema": {
                        "lat": {"type": "string"},
                        "lng": {"type": "string"}
                    }
                }
            }
        },
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "company": {
            "type": "dict",
            "schema": {
                "name": {"type": "string"},
                "catchPhrase": {"type": "string"},
                "bs": {"type": "string"}
            }
        }
    }),
])
def test_schema(url, schema):
    res = requests.get(url)

    v = cerberus.Validator()

    for item in res.json():
        assert v.validate(item, schema)


def test_json_1():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")

    with open("data_3_1.json") as f:
        expected_json = json.load(f)

    assert res.json() == expected_json


def test_json_2():
    res = requests.get("https://jsonplaceholder.typicode.com/albums")

    with open("data_3_2.json") as f:
        expected_json = json.load(f)

    assert res.json() == expected_json
