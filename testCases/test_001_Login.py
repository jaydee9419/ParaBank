from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import time


class Test_Login():

    url = ReadConfig.getApllicationURL()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(ReadConfig.getUsername())
        self.lp.setPassword(ReadConfig.getPassword())
        self.lp.clickLogin()

        time.sleep(10)
        self.driver.quit()

