from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class WikipediaHomePage(BasePage):
    SEARCH_FIELD = (By.NAME, 'search')

    def buscar_articulo(self, termino_busqueda):
        campo_busqueda = self.wait_for_element(self.SEARCH_FIELD)
        campo_busqueda.clear()
        campo_busqueda.send_keys(termino_busqueda)
        campo_busqueda.submit()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
