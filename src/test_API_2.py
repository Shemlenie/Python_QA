import pytest
import requests
import json
import conftest
import cerberus

TEMPLATE_SCHEMA = {
    "id": {"type": "string"},
    "name": {"type": "string"},
    "brewery_type": {"type": "string"},
    "street": {"type": "string"},
    "address_2": {"type": "string"},
    "address_3": {"type": "string"},
    "city": {"type": "string"},
    "state": {"type": "string"},
    "county_province": {"type": "string"},
    "postal_code": {"type": "string"},
    "country": {"type": "string"},
    "longitude": {"type": "string"},
    "latitude": {"type": "string"},
    "phone": {"type": "string"},
    "website_url": {"type": "string"},
    "updated_at": {"type": "string"},
    "created_at": {"type": "string"}
}


@pytest.mark.parametrize("url, status", [
    ("https://api.openbrewerydb.org/breweries", 200),
    ("https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati", 200),
    ("https://api.openbrewerydb.org/breweries/search?query=dog", 200),
    ("https://api.openbrewerydb.org/breweries/autocomplete?query=dog", 200)
])
def test_status_1(url, status):
    return conftest.test_url_status(url, status)


def test_status_2(base_url, status):
    return conftest.test_url_status("https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati12312312312",
                                    404)


@pytest.mark.parametrize("url, schema", [
    ("https://api.openbrewerydb.org/breweries?page=1&per_page=1", {
        "address_2": {"nullable": True},
        "address_3": {"nullable": True},
        "county_province": {"nullable": True},
        "website_url": {"nullable": True}}),
    ("https://api.openbrewerydb.org/breweries?page=2&per_page=1", {
        "address_2": {"nullable": True},
        "address_3": {"nullable": True},
        "county_province": {"nullable": True},
        "longitude": {"nullable": True},
        "latitude": {"nullable": True}}),
    ("https://api.openbrewerydb.org/breweries?page=3&per_page=1", {
        "address_2": {"nullable": True},
        "address_3": {"nullable": True},
        "county_province": {"nullable": True},
        "longitude": {"nullable": True},
        "latitude": {"nullable": True},
        "website_url": {"nullable": True}}),
    ("https://api.openbrewerydb.org/breweries?page=4&per_page=1", {
        "address_2": {"nullable": True},
        "address_3": {"nullable": True},
        "county_province": {"nullable": True},
        "website_url": {"nullable": True}}),
])
def test_schema(url, schema):
    res = requests.get(url)
    temp_dict = TEMPLATE_SCHEMA.copy()
    temp_dict.update(schema)

    v = cerberus.Validator()

    assert v.validate(res.json()[0], temp_dict)


def test_json_1():
    res = requests.get("https://api.openbrewerydb.org/breweries/search?query=dog")

    with open("data_2_1.json") as f:
        expected_json = json.load(f)

    assert res.json() == expected_json


def test_json_2():
    res = requests.get("https://api.openbrewerydb.org/breweries")

    with open("data_2_2.json") as f:
        expected_json = json.load(f)

    assert res.json() == expected_json
