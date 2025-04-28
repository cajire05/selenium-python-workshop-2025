from behave import given, when, then
from selenium import webdriver
from pages.home_page_mercado import MercadoLibreHomePage
from pages.results_page_mercado import MercadoLibreResultsPage

@given('el usuario se encuentra en la página principal de MercadoLibre')
def step_given_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co')
    context.driver.maximize_window()
    context.home_page = MercadoLibreHomePage(context.driver)

@when('el usuario busca "iPhone 13"')
def step_when_search_product(context):
    context.home_page.search_product("iPhone 13")
    context.results_page = MercadoLibreResultsPage(context.driver)

@then('aparecen resultados que contienen el texto "iPhone"')
def step_then_verify_results(context):
    assert context.results_page.results_contain_text("iPhone"), "El texto 'iPhone' no se encontró en los resultados."

