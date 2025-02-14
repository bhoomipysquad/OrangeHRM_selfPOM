import time
from Pages.HomePage import Home
from Test.test_login import Test_Login


class Test_Home(Test_Login):
    def test_sidemenu(self,setup):
        self.driver = setup
        self.hp = Home (self.driver)
        self.hp.click_admin()
        time.sleep(2)
        self.hp.click_pim()
        time.sleep(2)
        self.hp.click_my_info()
        time.sleep(2)
        self.hp.click_performance()
        time.sleep(2)
        self.hp.click_dashboard()
        time.sleep(2)
        self.hp.click_directory()
        time.sleep(2)
        self.hp.click_claim()
        time.sleep(2)
        self.hp.click_buzz()
        time.sleep(2)
        self.hp.click_maintenance()
        time.sleep(2)