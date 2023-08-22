from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class PickBuisness:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait




    def pick_buisness(self):
        sum_element = self.wait.until(EC.element_to_be_clickable((By.ID, "ember2143")))
        sum_element.click()
        time.sleep(3)
        sum_values = self.wait.until(EC.presence_of_all_elements_located((By.ID, "ember2498")))
        sum_values.send_keys("80")
        time.sleep(3)
        sum_element = self.wait.until(EC.element_to_be_clickable((By.ID, "ember2504")))
        sum_element.click()
