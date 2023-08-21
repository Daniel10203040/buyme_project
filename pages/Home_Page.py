from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.press_to_register = (By.CSS_SELECTOR, '.notSigned')
        self.press_registration = (
By.XPATH, '//span[@class="text-link theme" and @aria-label="להרשמה" and @role="link"]')
        self.elements_with_placeholder = (By.CSS_SELECTOR, "[placeholder]")
        self.policy_agreement = (By.TAG_NAME, "circle")