import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Login_page import LoginPage
from pages.Selection_Page import SelectionPage


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

        selection_page = SelectionPage(driver, wait)
        selection_page.select_sum()
        selection_page.select_region()
        selection_page.select_category()

        search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='איזו מתנה תרצו לחפש?']")))
        search_input.send_keys("פרחים")

        time.sleep(5)

        result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[value='17573218']")))
        result_element.click()

        wait.until(EC.element_to_be_clickable((By.ID, "ember1199"))).click()

        time.sleep(5)

        assert driver.find_element(By.CSS_SELECTOR,
                                   "h1").text == "לא נמצאו תוצאות חיפוש ל\"רוז פרחים\" במרכז בסכום עד 99 ש\"ח בקטגוריה מתנות למזל דלי"


