from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage
import time

scenarios('../../features/testcases_20250430_2341.feature')

@given("I am on the online store page")
def abrir_tienda(page):
    homepage = HomePage(page)
    homepage.abrir()

@when(parsers.parse('I enter "{producto}" in the search field'))
def escribir_producto(page, producto):
    homepage = HomePage(page)
    homepage.buscar_producto(producto)
    time.sleep(2)

@when("I click the search button")
def clic_buscar(page):
    pass  # ya se hace en buscar_producto()

@then(parsers.parse('I should see the product "{producto}" in the search results'))
def validar_resultado(page, producto):
    assert producto.lower() in page.inner_text("#center_column").lower()

@then("I should see a message indicating that no results were found for the search")
def validar_mensaje_no_encontrado(page):
    assert "No results were found" in page.inner_text("#center_column")
