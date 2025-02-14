import time
from Pages.LoginPage import Login
from Test.conftest import Base, baseURL
from utilities.custom_logger import LogGen


class Test_Login(Base):
    def test_dologin(self,setup):
        logger = LogGen.loggen()
        logger.info("**************** Test dologin ********************")
        logger.info("**************** verifying login page ********************")
        self.driver = setup
        time.sleep(8)
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        time.sleep(6)
        current_url = self.driver.current_url
        time.sleep(2)
        if baseURL == current_url:
            self.driver.save_screenshot("Login.png")
            logger.error("**************** login page case failed ********************")
            assert False
        else:
            assert True
            logger.info("**************** login page case passed ********************")


class Test_Logout(Test_Login):
    def test_logout(self,setup):
        self.test_dologin(setup)
        self.lp.click_logout()

