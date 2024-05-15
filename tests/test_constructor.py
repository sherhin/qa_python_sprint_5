from conftest import driver_client

from locators import Locators as locator
from data import Urls as url


class TestConstructor:

    def test_move_to_constructor_from_lk(self, driver_client):
        driver_client.get(url.registry_page)
        driver_client.find_element(*locator.constructor).click()
        assert driver_client.current_url == url.main_page

    def test_move_to_constructor_click_logo(self, driver_client):
        driver_client.get(url.registry_page)
        driver_client.find_element(*locator.logo_button).click()
        assert driver_client.current_url == url.main_page

    def test_move_to_buns(self, driver_client):
        driver_client.get(url.main_page)
        driver_client.find_element(*locator.sauces).click()
        buns = driver_client.find_element(*locator.buns)
        buns.click()
        current_class = buns.get_attribute('class')
        assert 'type_current' in current_class

    def test_move_to_sauces(self, driver_client):
        driver_client.get(url.main_page)
        sauces = driver_client.find_element(*locator.sauces)
        sauces.click()
        current_class = sauces.get_attribute('class')
        assert 'type_current' in current_class

    def test_move_to_ingredients(self, driver_client):
        driver_client.get(url.main_page)
        ingredients = driver_client.find_element(*locator.ingredients)
        ingredients.click()
        current_class = ingredients.get_attribute('class')
        assert 'type_current' in current_class
