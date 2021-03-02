import time
from selenium.webdriver.common.by import By
from SampleProjects.POMDemo.Locators.locators import Locators


class LoginPages:
    def __init__(self, driver):
        self.driver = driver

        self.login_Button = '//*[@id="js--main-header"]/div/div/div[3]/div/div[2]/a'
        self.user_name = "j_username"
        self.password = "j_password"
        self.sign_in_button = '//*[@id="loginForm"]/button'


def click_sign_in_button(self):
    time.sleep(2)
    self.driver.find_element(By.XPATH, Locators.login_Button).click()


def enter_user_name(self, username):
    self.driver.find_element_by_id(Locators.user_name).clear
    time.sleep(2)
    self.driver.find_element_by_id(Locators.user_name).send_keys(username)


def enter_password(self, password):
    self.driver.find_element_by_id(Locators.password).clear
    time.sleep(2)
    self.driver.find_element_by_id(Locators.password).send_keys(password)


def click_login_button(self):
    time.sleep(2)
    self.driver.find_element(By.XPATH, Locators.sign_in_button).click()
