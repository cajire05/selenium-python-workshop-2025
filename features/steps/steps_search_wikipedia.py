from behave import given, when, then
from selenium import webdriver
from pages.home_page_wikipedia import WikipediaHomePage
from pages.article_page_wikipedia import WikipediaArticlePage

@given('el usuario se encuentra en la página principal de Wikipedia')
def step_open_wikipedia_home(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://es.wikipedia.org')
    context.driver.maximize_window()
    context.home_page = WikipediaHomePage(context.driver)

@when('el usuario busca "Python (lenguaje de programación)"')
def step_search_article(context):
    context.home_page.buscar_articulo("Python (lenguaje de programación)")
    context.article_page = WikipediaArticlePage(context.driver)

@then('el título del artículo debe ser "Python (lenguaje de programación)"')
def step_validate_article_title(context):
    titulo_encontrado = context.article_page.obtener_titulo_articulo()
    expected_title = "Python"
    assert titulo_encontrado == expected_title, "El título no coincide."
