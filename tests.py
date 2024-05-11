import pytest

from selenium.webdriver.common.by import By

from data import Selectors as selector
from data import Urls as url
from data import Credetionals as cred


@pytest.mark.usefixtures('driver_client', 'delete_all_cookies')
class TestRegistration:

    def test_account_button_from_main_page(self, driver_client, browser_helper):
        personal_account_page = browser_helper.get_personal_account_page_logout(driver_client)
        assert personal_account_page

    def test_registration_button_is_clickable(self, driver_client, browser_helper):
        registry_page = browser_helper.get_registration_page(driver_client)
        assert registry_page

    def test_registration_correct_values(self, browser_helper, driver_client):
        cred.email = cred().unique_email()
        registry_status, email, password = browser_helper.registration(
            driver_client, cred.login, cred.email, cred.password
        )
        assert registry_status

    @pytest.mark.parametrize('email, password, login', [
        ('', '456789', 'tevmenova'), (cred().unique_email(), '1', 'tevmenova')])
    def test_registration_incorrect_values(self, driver_client, browser_helper, email, password, login):
        registry_status, email, password = browser_helper.registration(
            driver_client, login, email, password
        )
        assert not registry_status

    def test_logout(self, browser_helper, driver_incognito):
        email = cred().unique_email()
        registry_status, email, password = browser_helper.registration(
            driver_incognito, cred.login, email, cred.password)
        browser_helper.authorization(driver_incognito, email, cred.password)
        logout_status = browser_helper.logout(driver_incognito)
        assert logout_status

    @pytest.mark.parametrize('from_page', [url.main_page, url.authorization_page, url.forgot_passwod_page])
    def test_authorization_from_page(self, browser_helper, driver_incognito, from_page):
        email = cred().unique_email()
        registry_status, email, password = browser_helper.registration(
            driver_incognito, cred.login, email, cred.password
        )
        if registry_status:
            auth_status = browser_helper.authorization(driver_incognito, email, password, from_page=from_page)
            assert auth_status


@pytest.mark.usefixtures('driver_client', 'delete_all_cookies', 'authorize')
class TestConstructor:

    def test_move_to_constructor_from_lk(self, driver_client, browser_helper):
        browser_helper.get_profile_page(driver_client)
        constructor_button = selector.constructor
        driver_client.find_element(By.XPATH, constructor_button).click()
        assert driver_client.current_url == url.main_page

    def test_move_to_constructor_click_logo(self, driver_client, browser_helper):
        browser_helper.get_profile_page(driver_client)
        logo_button = selector.logo_button
        driver_client.find_element(By.XPATH, logo_button).click()
        assert driver_client.current_url == url.main_page

    def test_move_to_categories(self, driver_client, browser_helper):
        driver_client.get(url.main_page)
        categories = [selector.sauces, selector.buns, selector.ingredients]
        for category in categories:
            element = (By.XPATH, category)
            button = browser_helper.wait_element_is_presence(driver_client, element)
            button.click()
            current_class = driver_client.find_element(By.XPATH, category).get_attribute('class')
            assert 'type_current' in current_class
