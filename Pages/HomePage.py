from selenium.webdriver.common.by import By

class Home:

    admin_linktext = "Admin"
    PIM_linktext = "PIM"
    Recruitment_linktext = "Recruitment"
    My_info_linktext = "My Info"
    Performance_linktext = "Performance"
    Dashboard_linktext  = "Dashboard"
    Directory_linktext = "Directory"
    Maintenance_linktext = "Maintenance"
    claim_linktext = "Claim"
    Buzz_linktext = "Buzz"


    def __init__(self,driver):
        self.driver = driver

    def click_admin(self):
        self.driver.find_element(By.LINK_TEXT,self.admin_linktext).click()

    def click_PIM(self):
        self.driver.find_element(By.LINK_TEXT,self.PIM_linktext).click()

    def click_My_info(self):
        self.driver.find_element(By.LINK_TEXT,self.My_info_linktext).click()

    def click_Performance(self):
        self.driver.find_element(By.LINK_TEXT,self.Performance_linktext).click()

    def click_Dashboard(self):
        self.driver.find_element(By.LINK_TEXT,self.Dashboard_linktext).click()

    def click_Directory(self):
        self.driver.find_element(By.LINK_TEXT,self.Directory_linktext).click()

    def click_Maintenance(self):
        self.driver.find_element(By.LINK_TEXT,self.Maintenance_linktext).click()

    def click_claim(self):
        self.driver.find_element(By.LINK_TEXT,self.claim_linktext).click()

    def click_Buzz(self):
        self.driver.find_element(By.LINK_TEXT,self.Buzz_linktext).click()