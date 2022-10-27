from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
from selenium import webdriver
import logging
import datetime


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base_url", default="http://192.168.100.3:8081/")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--exec", action="store", default="172.18.96.1")


@pytest.fixture
def executer(request):
    brw_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    log_level = request.config.getoption("--log_level")
    exec = request.config.getoption("--exec")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    if exec == "local":
        if brw_name == "chrome":
            serv = ChromeService(executable_path="C:/driv/chrome/chromedriver")
            driver = webdriver.Chrome(service=serv)

        elif brw_name == "firefox":
            driver = webdriver.Firefox(executable_path="C:/driv/geckodriver")

        elif brw_name == "opera":
            driver = webdriver.opera(executable_path="C:/driv/operadriver")

        else:
            raise ValueError("Browser is not supported")

    else:
        driver = webdriver.Remote(
            command_executor=f"http://{exec}:4444/wd/hub",
            desired_capabilities={"browserName": brw_name, "platformName": "Windows 10"}
        )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    driver.base_url = base_url
    return driver

    def closing():
        driver.quit()

    request.addfinalizer(closing)
    return driver
