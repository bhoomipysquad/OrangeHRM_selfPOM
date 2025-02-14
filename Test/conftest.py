from selenium import webdriver
import pytest

baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseURL)
    return driver


class Base:
   username = "Admin"
   password = "admin123"
