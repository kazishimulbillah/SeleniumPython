import time
from selenium.webdriver.common.by import By
from SampleProjects.POMDemo.Locators.locators import Locators


class HomePages:

    def __init__(self, driver):
        self.driver = driver

        self.logo = '//*[@id="js--main-header"]/div/div/div[1]/div/a/img'
        self.login_message = '//*[@id="js--message"]/p'

    def goto_home_page(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.logo).click()

    def check_login_message(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login_message).text
        print(self.driver.find_element(By.XPATH, self.login_message).text)
