import time
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from SampleProjects.POMDemo.Pages.LoginPage import LoginPages
from SampleProjects.POMDemo.Pages.HomePage import HomePages


@classmethod
class LoginTest(unittest.TestCase):

    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:/AutomationConfig/DRIVER/chromedriver.exe")
        time.sleep(2)
        self.driver.maximize_window()

    def test_login_valid(self):
        driver1 = self.driver

        time.sleep(2)
        driver1.get("https://www.rokomari.com/book")

        login = LoginPages(driver1)
        time.sleep(2)
        login.click_sign_in_button()

        time.sleep(2)
        login.enter_user_name("shimulece07@gmail.com")

        time.sleep(2)
        login.enter_password("shimul@1234")

        time.sleep(2)
        login.click_login_button()

        homepage = HomePages(driver1)

        time.sleep(2)
        homepage.check_login_message()

        time.sleep(2)
        homepage.goto_home_page()

    @classmethod
    def tearDownClass(cls):
        cls.river.close()
        cls.driver.quit()
