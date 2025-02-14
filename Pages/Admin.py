import time
from selenium.webdriver.common.by import By


class Admin():
    def __init__(self,driver):
        self.driver = driver

    admin_linktext = "Admin"
    User_management_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
    users_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul'
    def click_user_management(self):
        self.driver.find_element(By.LINK_TEXT, self.admin_linktext).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.User_management_xpath).click()
        self.driver.find_element(By.XPATH, self.users_xpath).click()
        time.sleep(2)



    job_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]'
    def click_job(self):
         self.driver.find_element(By.XPATH, self.job_xpath).click()
         time.sleep(2)
         Job = {       'job_titles_xpath' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]',
                      'pay_grades_xpath' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]',
                      'employement_status_xpath' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]/a[1]',
                      'job_categories_xpath' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]',
                      'work_shift_xpath' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]'
                }
         for menu,xpath in Job.items():
             try:
                 element = self.driver.find_element(By.XPATH,xpath)
                 element.click()
                 time.sleep(3)
                 self.driver.find_element(By.XPATH, self.job_xpath).click()
                 time.sleep(3)
             except Exception as e:
                 print(f"Error occurred while clicking {menu}: {e}")



    organization_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]'
    def click_organization(self):
        self.driver.find_element(By.XPATH, self.organization_xpath).click()
        time.sleep(2)
        organization = {     'general_information_xpath' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a',
                             'locations_xpath' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]',
                             'structure_xpath' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]/a'
                       }
        for menu1,xpath in organization.items():
              try:
                 felement = self.driver.find_element(By.XPATH,xpath)
                 felement.click()
                 time.sleep(3)
                 self.driver.find_element(By.XPATH, self.organization_xpath).click()
                 time.sleep(3)
              except Exception as e:
                 print(f"Error occurred while clicking {menu1}: {e}")



    qualifications_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]'
    def click_qualifications(self):
        self.driver.find_element(By.XPATH, self.qualifications_xpath).click()
        time.sleep(2)
        qualifications = {  'skills' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]',
                            'Education' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]',
                            'Licenses' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[3]',
                            'Languages' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[4]',
                            'Memberships' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[5]'
                         }
        for menu2,xpath in qualifications.items():
            try:
                qelement = self.driver.find_element(By.XPATH,xpath)
                qelement.click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, self.qualifications_xpath).click()
                time.sleep(3)
            except Exception as e:
                print(f"Error occurred while clicking {menu2}: {e}")



    nationalities_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]'
    def click_nationalities(self):
        self.driver.find_element(By.XPATH, self.nationalities_xpath).click()
        time.sleep(2)



    corporate_branding_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]'
    def click_corporate_branding(self):
        self.driver.find_element(By.XPATH, self.corporate_branding_xpath).click()
        time.sleep(2)



    configuration_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]'
    def click_configuration(self):
        self.driver.find_element(By.XPATH,self.configuration_xpath).click()
        time.sleep(2)
        configuration = {  'Email Configuration' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[1]',
                           'Email subscription' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[2]',
                           'Localization' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[3]',
                           'Languages packages' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[4]',
                           'Modules' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[5]',
                           'social media authentication' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[6]',
                           'register 0auth client' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[7]',
                           'LDAP configuration' : '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[8]'
                        }
        for menu3,xpath in configuration.items():
            try:
                celement = self.driver.find_element(By.XPATH,xpath)
                celement.click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, self.qualifications_xpath).click()
                time.sleep(3)
            except Exception as e:
                print(f"Error occurred while clicking {menu3}: {e}")





