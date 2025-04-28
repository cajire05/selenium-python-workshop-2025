from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class MercadoLibreHomePage(BasePage):
    SEARCH_INPUT = (By.NAME, 'as_word')

    def search_product(self, product_name):
        search_box = self.wait_for_element(self.SEARCH_INPUT)
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.submit()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
