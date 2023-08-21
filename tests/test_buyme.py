from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.Login_page import LoginPage


class TestBuyMe:

    def test_Login(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver,20)
        login = LoginPage(driver,wait)
        driver.get("https://buyme.co.il/")
        login.register("daniel","daniel@gmail.com","Pass123")

