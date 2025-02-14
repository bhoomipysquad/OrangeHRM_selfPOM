import time
from Pages.Admin import Admin
from Test.test_login import Test_Login


class Test_Admin(Test_Login):
    def test_admin(self,setup):
        self.driver = setup
        self.ad = Admin (self.driver)
        time.sleep(5)
        self.ad.click_user_management()
        time.sleep(2)
        self.ad.click_job()
        time.sleep(6)
        self.ad.click_organization()
        time.sleep(2)
        self.ad.click_qualifications()
        time.sleep(2)
        self.ad.click_nationalities()
        time.sleep(2)
        self.ad.click_corporate_branding()
        time.sleep(2)
        self.ad.click_configuration()
        time.sleep(2)

