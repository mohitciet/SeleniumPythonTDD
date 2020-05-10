import pytest
from base.webdriverfactory import WebDriverFactory
import utilities.custom_logger as cl
import logging



# @pytest.yield_fixture()
# @pytest.fixture(scope="method")
# def classSetUp():
#     print("Running class level setUp")
#     yield
#     print("Running class level tearDown")

@pytest.yield_fixture()
#@pytest.fixture(scope="class")
def methodSetUp(request, browser):
    print("Running method setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running method tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")