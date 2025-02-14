from selenium.webdriver.common.by import By

from Test.conftest import Base


class Login(Base):

    text_username_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
    text_password_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
    button_login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    dropdown_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i'
    logout_xpath = "//a[normalize-space()='Logout']"


    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.dropdown_xpath).click()
        self.driver.find_element(By.XPATH,self.logout_xpath).click()