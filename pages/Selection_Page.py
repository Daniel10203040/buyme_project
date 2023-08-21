from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SelectionPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def select_sum():
        sum_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='סכום']")))
        sum_element.click()
        time.sleep(1)
        sum_values = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[value='1']")))
        sum_values[1].click()

    def select_region():
        region_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='אזור']")))
        region_element.click()
        time.sleep(5)
        region_values = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[value='11']")))
        region_values[1].click()

    def select_category():
        category_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='קטגוריה']")))
        category_element.click()
        category_values = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[value='358']")))
        category_values[1].click()

