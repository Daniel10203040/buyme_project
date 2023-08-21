from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.press_to_register = (By.CSS_SELECTOR, '.notSigned')
        self.press_registration = (
By.XPATH, '//span[@class="text-link theme" and @aria-label="להרשמה" and @role="link"]')
        self.elements_with_placeholder = (By.CSS_SELECTOR, "[placeholder]")
        self.policy_agreement = (By.TAG_NAME, "circle")

    def register(self, first_name, email, password):
        self.wait.until(EC.element_to_be_clickable(self.press_to_register)).click()

        # Click on the registration link
        press_registration = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.press_registration))
        press_registration.click()

        # Fill in the registration form
        elements_with_placeholder = self.driver.find_elements(*self.elements_with_placeholder)
        elements_with_placeholder[0].send_keys(first_name)
        elements_with_placeholder[1].send_keys(email)
        elements_with_placeholder[2].send_keys(password)
        elements_with_placeholder[3].send_keys(password)

        # Click the policy agreement checkbox
        PolicyAgreement = self.driver.find_element(*self.policy_agreement)
        PolicyAgreement.click()

        # Submit the registration form
        Submit1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ember1948")))
        Submit1.click()

        # Add a sleep for demonstration purposes (consider using waits)
        time.sleep(3)