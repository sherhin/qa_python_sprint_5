from selenium.common import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_client
from data import Credetionals
from data import Urls as url
from locators import Locators as locator


class TestRegistration:

    def test_registration_correct_values(self, driver_client):
        cred = Credetionals()
        driver_client.get(url.registry_page)
        email = cred.email
        login = cred.login
        password = cred.password
        email_field = driver_client.find_element(*locator.email_field)
        login_field = driver_client.find_element(*locator.name_field)
        password_field = driver_client.find_element(*locator.password_field)
        email_field.send_keys(email)
        login_field.send_keys(login)
        password_field.send_keys(password)
        driver_client.find_element(*locator.registry_button).click()
        try:
            reg_status = WebDriverWait(
                driver_client, 5).until(EC.url_to_be(url.authorization_page))
        except TimeoutException:
            reg_status = False
        assert reg_status

    def test_registration_incorrect_password(self, driver_client):
        driver_client.get(url.registry_page)
        password_field = driver_client.find_element(*locator.password_field)
        password_field.send_keys('1')
        driver_client.find_element(*locator.registry_button).click()
        assert driver_client.find_element(*locator.input_error)
