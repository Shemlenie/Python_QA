import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store",  choises=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="127.0.0.1:8081")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        driver = webdriver.Chrome()
    elif _browser == "opera":
        driver = webdriver.Opera()
    elif _browser == "firefox":
        driver = webdriver.Firefox()

    return driver
