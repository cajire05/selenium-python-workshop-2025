from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class WikipediaArticlePage(BasePage):
    ARTICLE_TITLE = (By.ID, 'firstHeading')

    def obtener_titulo_articulo(self):
        titulo = self.wait_for_element(self.ARTICLE_TITLE)
        return titulo.text.strip()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
