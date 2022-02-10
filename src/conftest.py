import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default="200",
        choices=["200", "300", "400", "404", "500", "502", "503"],
        help="Status code"
    )

    # parser.addoption(
    #     "--method",
    #     default="get",
    #     choices=["get", "post", "put", "patch", "delete"],
    #     help="Method to execute"
    # )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status(request):
    return request.config.getoption("--status_code")

# @pytest.fixture
# def request_method(request):
#     return getattr(requests, request.config.getoption("--method"))

def test_url_status(base_url, status):
    response = requests.get(url=base_url)
    print(response.status_code)
    assert response.status_code == int(status)
