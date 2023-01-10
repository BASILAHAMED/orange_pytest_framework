"""
Sample Testcase

Test case ID: TC_Login_01
Test objective:
Successful Employee login to OrangeHRM portal

Precondition:
1. A valid ESS-User account to login to be available
2. Orange HRM 3.0 site is launched on a compatible browser

Steps:
1. In the login Panel, enter the username (Test Data: "Admin")
2. Enter the Password for the ESS-User account in the password field (Test data: "admin123")
3. Click "Login" button

Expected Result:
The user is logged in successfully."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestLogin():
    def tc_login_01(self):
        # launching chrome driver
        driver = webdriver.Chrome()

        # loading orange_hrm webpage
        orange_hrm_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(orange_hrm_url)

        # maximize browser window
        driver.maximize_window()
        time.sleep(5)

        # input username
        xpath_of_username = '//input[@name="username"]'
        input_username = driver.find_element(By.XPATH, xpath_of_username)
        input_username.send_keys("Admin")
        time.sleep(5)

        # input password
        xpath_of_password = '//input[@type="password"]'
        input_password = driver.find_element(By.XPATH, xpath_of_password)
        input_password.send_keys("admin123")
        time.sleep(5)

        # click login button
        xpath_of_loginbutton = '//button[@type="submit"]'
        click_loginbutton = driver.find_element(By.XPATH, xpath_of_loginbutton)
        click_loginbutton.click()
        time.sleep(8)

        # verify successful login
        xpath_of_dashboard = '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]'
        fetch = driver.find_element(By.XPATH, xpath_of_dashboard)
        dashboard = fetch.text
        if dashboard == "Dashboard":
            print("The user is logged in successfully")
        else:
            print("Invalid credentials")

        # close driver instance
        driver.close()

TL = TestLogin()
TL.tc_login_01()

