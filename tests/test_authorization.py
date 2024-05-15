from selenium.common import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_client
from data import Credetionals
from data import Urls as url
from locators import Locators as locator


class TestAuthorization:

    @staticmethod
    def prepare_test_data(driver_client):
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
                driver_client,5).until(EC.url_to_be(url.authorization_page)
            )
        except TimeoutException:
            reg_status = False
        assert reg_status
        return email, password


    def test_authorization_from_main_page(self, driver_client):
        email, password = self.prepare_test_data(driver_client)
        driver_client.get(url.main_page)
        driver_client.find_element(*locator.account_button).click()
        WebDriverWait(driver_client, 5).until(EC.url_to_be(url.authorization_page))
        driver_client.find_element(*locator.email_field).send_keys(email)
        driver_client.find_element(*locator.password_field).send_keys(password)
        button_to_click = WebDriverWait(driver_client, 5).until(EC.presence_of_element_located(locator.enter_button))
        button_to_click.click()
        try:
            auth_status = WebDriverWait(driver_client, 10).until(EC.url_to_be(url.main_page))
        except TimeoutException:
            auth_status = False
        assert auth_status

    def test_authorization_from_authorization_page(self, driver_client):
        email, password = self.prepare_test_data(driver_client)
        driver_client.get(url.authorization_page)
        driver_client.find_element(*locator.email_field).send_keys(email)
        driver_client.find_element(*locator.password_field).send_keys(password)
        button_to_click = WebDriverWait(driver_client, 5).until(EC.presence_of_element_located(locator.enter_button))
        button_to_click.click()
        try:
            auth_status = WebDriverWait(driver_client, 10).until(EC.url_to_be(url.main_page))
        except TimeoutException:
            auth_status = False
        assert auth_status

    def test_authorization_from_forgot_password_page(self, driver_client):
        email, password = self.prepare_test_data(driver_client)
        driver_client.get(url.forgot_password_page)
        driver_client.find_element(*locator.lk_button).click()
        driver_client.find_element(*locator.email_field).send_keys(email)
        driver_client.find_element(*locator.password_field).send_keys(password)
        button_to_click = WebDriverWait(driver_client, 5).until(EC.presence_of_element_located(locator.enter_button))
        button_to_click.click()
        try:
            auth_status = WebDriverWait(driver_client, 10).until(EC.url_to_be(url.main_page))
        except TimeoutException:
            auth_status = False
        assert auth_status
