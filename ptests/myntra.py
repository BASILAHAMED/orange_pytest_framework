# import time
#
# import pytest
# from selenium.webdriver import ActionChains, Keys
#
# from pageObject.myntrahomepage import myntrahomepage
# from pageObject.myntraloggedinpage import myntraloggedinpage
# from pageObject.myntraloginpage import myntraloginpage
# from pageObject.myntrapasswordenter import myntrapasswordenter
# from pageObject.myntrapasswordotp import myntrapasswordotp
# from pageObject.myntrasareeselection import myntrasareeselection
# from selenium.webdriver.common.by import By
# from utilities.BaseClass import BaseClass
#
#
# class Testmyntra(BaseClass):
#
#     def test_add_saree_to_cart(self):
#         log = self.get_logger()
#         # myntra home page
#         A = ActionChains(self.driver)
#         mhp = myntrahomepage(self.driver)
#         mhp_profile_ele = mhp.profile_login()
#         log.info("Hovering over profile button")
#         A.move_to_element(mhp_profile_ele).perform()
#         log.info("Successfully performed hovering action on login button")
#         mhp_lgn_btn = mhp.login_b()
#         self.verify_element_clickable("//a[@href='/login?referer=https://www.myntra.com/']")
#         A.move_to_element(mhp_lgn_btn).click().perform()
#         log.info("Entered login page")
#
#         # myntra login page
#         mlp = myntraloginpage(self.driver)
#         time.sleep(5)
#         num_inp = mlp.enter_number()
#         log.info("Enter the number")
#         num_inp.send_keys(7416416647)
#         log.info("Number entered")
#         num_inp.send_keys(Keys.ENTER)
#         #time.sleep(5)
#         #self.verify_element_presence('/html/body/div/div/span')
#         #self.verify_element_absence('/html/body/div/div/span')
#         time.sleep(50)
#         #self.verify_element_presence('//div[text()="CONTINUE"]')
#         #time.sleep(5)
#         #self.verify_element_absence('message-text')
#         num_inp.send_keys(Keys.ENTER)
#         log.info("Navigating to password otp page")
#         # time.sleep(30)
#
#         # myntra password otp
#         mpo = myntrapasswordotp(self.driver)
#         self.verify_element_clickable("//div[@class='bottomeLink']/span")
#         mpo.password_option()
#             #log.info("You might potentially exceeded the OTP count kindly wait for 30 min")
#
#         # myntra enter password
#         mpe = myntrapasswordenter(self.driver)
#         e_p = mpe.enterpassword()
#         e_p.send_keys("Build@234")
#         e_p.send_keys(Keys.ENTER)
#
#         # myntra loggedin page
#         mlgd = myntraloggedinpage(self.driver)
#         self.verify_element_clickable("//div[@data-reactid='179']/a")
#         mlgd.women()
#         self.verify_element_clickable("//li[@data-reactid='193']/a")
#         mlgd.saree()
#
#         #myntrasareeselection
#         mss = myntrasareeselection(self.driver)
#         self.verify_element_clickable('//a[@href="sarees/united-liberty/united-liberty-teal-blue--golden-zari-art-silk'
#                               '-banarasi-saree/17703594/buy"]')
#         mss.clickonitem()
#         #Windows_opened = self.driver.window_handles
#         #self.driver.switch_to.window(Windows_opened[1])
#         #get_title = self.driver.title
#         #print(get_title)
#         #time.sleep(10)
#         #self.verify_element_clickable('//span[@class="myntraweb-sprite pdp-whiteBag sprites-whiteBag pdp-flex pdp-center"]')
#         mss.addtocart()
#
#
#         conclusion = ''
#         time.sleep(5)
#         conclusion = self.driver.find_element(By.XPATH,"//div[text()='PLACE ORDER']")
#         print(conclusion)
#
#         assert conclusion.text == 'PLACE ORDER'
