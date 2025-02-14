import time
from Pages.HomePage import Home
from Test.test_login import Test_Login


class Test_Home(Test_Login):
    def test_sidemenu(self,setup):
        self.driver = setup
        self.hp = Home (self.driver)
        self.hp.click_admin()
        time.sleep(2)
        self.hp.click_PIM()
        time.sleep(2)
        self.hp.click_My_info()
        time.sleep(2)
        self.hp.click_Performance()
        time.sleep(2)
        self.hp.click_Dashboard()
        time.sleep(2)
        self.hp.click_Directory()
        time.sleep(2)
        self.hp.click_claim()
        time.sleep(2)
        self.hp.click_Buzz()
        time.sleep(2)
        self.hp.click_Maintenance()
        time.sleep(2)