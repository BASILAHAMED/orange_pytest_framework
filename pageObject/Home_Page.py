from selenium.webdriver.common.by import By


class Home_Page:

    def __init__(self,driver):
        self.driver = driver

    username1 = (By.XPATH, '//input[@name="username"]')
    password1 = (By.XPATH, '//input[@type="password"]')
    login1 = (By.XPATH, '//button[@type="submit"]')
    dashboard1 = (By.XPATH, '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')

    def username(self):
        return self.driver.find_element(*Home_Page.username1)

    def password(self):
        return self.driver.find_element(*Home_Page.password1)

    def login(self):
        return self.driver.find_element(*Home_Page.login1)

    def dashboard(self):
        return self.driver.find_element(*Home_Page.dashboard1)

