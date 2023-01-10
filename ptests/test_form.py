import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.Home_Page import Home_Page
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_login(self, getData):
        # service_obj = Service(r"C:\Users\Lenovo\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
        # driver: WebDriver = webdriver.Chrome(service=service_obj)
        log = self.get_logger()
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        home_page = Home_Page(self.driver)
        # self.driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        home_page.username().send_keys(getData["username"])
        # self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        home_page.password().send_keys(getData["password"])
        # self.driver.find_element(By.ID, "exampleCheck1").click()
        home_page.login().click()
        time.sleep(5)

        # driver.find_element_by_xpath("//input[@type='submit']").click()
        # message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        message = home_page.dashboard().text
        log.info(message)
        assert "Dashboard" in message
        self.driver.refresh()

        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello again")
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        log.info("-----------------------TEST CASE ENDED--------------------------")

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param

