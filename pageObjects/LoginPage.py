import os.path

from selenium.webdriver.common.by import By

class LoginPage():
    input_username_xpath = "//input[@name='username']"
    input_password_xpath = "//input[@name='password']"
    btn_login_xpath = "//input[@value='Log In']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, uname):
        self.driver.find_element(By.XPATH, self.input_username_xpath).send_keys(uname)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
        self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//123.png")
