from behave import given, when, then
from selenium import webdriver
from pages.login_icesi import IntuLogin

@given('el usuario se encuentra en la pagina de login de intu')
def step_given_intu_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.icesi.edu.co/moodle/login/index.php')
    context.login_icesi = IntuLogin(context.driver)

@when('el usuario escrobe credenciales erroneas')
def step_when_intu_login(context):
    context.login_icesi.login("1105364621", "ewrewrwewr")

@then('aparece un mensaje de error')
def step_then_intu_login(context):
    assert "Acceso inválido. Por favor, inténtelo otra vez." == context.login_icesi.isElementPresent()

