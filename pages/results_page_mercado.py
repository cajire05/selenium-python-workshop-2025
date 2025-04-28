from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class MercadoLibreResultsPage(BasePage):
    FIRST_RESULT = (By.XPATH, '(//h2)[1]')

    def results_contain_text(self, text):
        first_result = self.wait_for_element(self.FIRST_RESULT)
        return text.lower() in first_result.text.lower()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
