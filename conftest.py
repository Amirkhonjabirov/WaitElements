from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base_url", default="http://192.168.100.3:8081/")


@pytest.fixture
def executer(request):
    brw_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")

    if brw_name == "chrome":
        serv = ChromeService(executable_path="C:/driv/chrome/chromedriver", )
        driver = webdriver.Chrome(service=serv)

    elif brw_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:/driv/geckodriver")

    elif brw_name == "opera":
        driver = webdriver.opera(executable_path="C:/driv/operadriver")

    else:
        raise ValueError("Browser is not supported")

    driver.base_url = base_url
    return driver

    driver.close()
