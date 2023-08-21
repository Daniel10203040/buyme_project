from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Login_page import LoginPage


class TestBuyMe:

    def test_register_existing_user(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver,20)
        login = LoginPage(driver,wait)
        driver.get("https://buyme.co.il/")
        login.register("daniel","danielsh741@gmail.com","Daniel102030")

        error_div = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-error")))

        # Get the text of the error div
        error_text = error_div.text

        # Assert that the error text contains the expected message
        expected_message = "דוא\"ל זה כבר קיים במערכת."
        assert expected_message in error_text, f"Expected message '{expected_message}' not found in error text: '{error_text}'"



    def test_login(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver,20)
        login = LoginPage(driver,wait)
        driver.get("https://buyme.co.il/")
        login.login("danielsh741@gmail.com","Daniel102030")