from selenium import webdriver
import pytest
import time


def pytest_addoption(parser):
    parser.addoption(
        "--browser_Name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_Name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(5)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

    elif browser_name == "edge":
        driver = webdriver.Edge()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

