import time
from Test.conftest import baseURL


class Test_BaseURL():
    def test_openurl(self, setup):
        self.driver = setup
        self.driver.get(baseURL)
        time.sleep(10)
        act_title = self.driver.title
        if act_title == "OrangeHRM":
          assert True
          self.driver.close()
        else:
          self.driver.save_screenshot("openurl.png")
          assert False