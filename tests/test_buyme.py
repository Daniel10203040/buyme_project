import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Login_page import LoginPage
from pages.Selection_Page import SelectionPage
from pages.Pick_Business_Page import PickBuisness


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
        login.login("danielsh741@gmail.com","Daniel123")

        selection_page = SelectionPage(driver, wait)
        selection_page.select_sum()
        selection_page.select_region()
        selection_page.select_category()

        search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='איזו מתנה תרצו לחפש?']")))
        search_input.send_keys("קלארו")

        time.sleep(5)



        result_element = wait.until(EC.visibility_of_element_located((By.ID, "ember1201")))
        result_element.click()

        wait.until(EC.element_to_be_clickable((By.ID, "ember1199"))).click()

        expected_url = "https://buyme.co.il/search?budget=1&category=438&query=%D7%A7%D7%9C%D7%90%D7%A8%D7%95&region=11"
        current_url = driver.current_url
        assert current_url == expected_url, f"URL assertion failed. Expected: {expected_url}, Actual: {current_url}"

        time.sleep(5)

        assert driver.find_element(By.CSS_SELECTOR,
                                   "h1").text == "לא נמצאו תוצאות חיפוש ל\"פרחים\" במרכז בסכום עד 99 ש\"ח בקטגוריה המתנות האהובות של 2023"



    def test_Pick_business(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver,20)
        login = LoginPage(driver,wait)
        driver.get("https://buyme.co.il/")
        login.login("danielsh741@gmail.com","Daniel123")


        pick_bussiness_page = PickBuisness(driver, wait)
        pick_bussiness_page.pick_buisness()

    def test_select_gift(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 20)
        login = LoginPage(driver, wait)
        driver.get("https://buyme.co.il/")
        login.login("danielsh741@gmail.com", "Daniel123")

        time.sleep(10)
        selection_page = SelectionPage(driver, wait)
        selection_page.select_sum()
        selection_page.select_category()
        selection_page.select_region()

        wait.until(EC.element_to_be_clickable((By.ID, "ember1199"))).click()
        time.sleep(5)

        # Click on the first subtitle
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".bm-subtitle-1")))[0].click()

        # Enter the amount
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='הכנס סכום']"))).send_keys(
            "50")

        # Wait for the presence of all submit buttons and click the first one
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[type=submit]")))[0].click()

        time.sleep(5)

        # Click on the first subtitle again
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".bm-subtitle-1")))[0].click()

        # Enter the amount again
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='הכנס סכום']"))).send_keys(
            "50")

        # Click on the first submit button again
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[type=submit]")))[0].click()

        time.sleep(5)

        # Enter the name of the recipient
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-parsley-required-message='מי הזוכה המאושר? יש להשלים את שם המקבל/ת']"))).send_keys(
            "daniel")

        # Click on the "לאיזה אירוע?" element
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[title='לאיזה אירוע?']"))).click()

        time.sleep(5)

        # Click on the second element with value "10"
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[value='10']")))[1].click()

        # Clear and enter a greeting
        greeting_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-parsley-group='voucher-greeting']")))
        greeting_element.clear()
        greeting_element.send_keys("mazal tov")

        # Upload a file
        driver.find_element(By.CSS_SELECTOR, "input[name=logo]").send_keys("tests/dog.jpg")

        # Click on the submit button
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type=submit]"))).click()

        # Click on the "עכשיו" element
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[gtm='עכשיו']"))).click()

        # Click on the "method-sms" element
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[gtm='method-sms']"))).click()

        # Clear and enter a mobile number
        mobile_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='נייד מקבל/ת המתנה']")))
        mobile_element.clear()
        mobile_element.send_keys("0547905728")

        # Clear and enter the sender's name
        sender_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='שם שולח המתנה']")))
        sender_element.clear()
        sender_element.send_keys("daniel")

        # Clear and enter a mobile number
        mobile_number_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='מספר נייד']")))
        mobile_number_element.clear()
        mobile_number_element.send_keys("0547905728")
        time.sleep(5)


