import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys

sys.path.append("/Users/chandrashekarbasavaraj/POMbasedproject")
from PageObject.loginpage import LoginPage


class Logintest(unittest.TestCase):
    baseURL = "http://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        #  lp.setUserName(self.username)
        # lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title is not matching")
        time.sleep(3)
        lp.clickLogout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/chandrashekarbasavaraj/POMbasedproject/Reports"))
