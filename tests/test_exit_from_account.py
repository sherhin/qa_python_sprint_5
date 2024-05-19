from selenium.common import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_client
from data import Credetionals
from data import Urls as url
from locators import Locators as locator


class TestExitFromAccount:

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
                driver_client, 5).until(EC.url_to_be(url.authorization_page)
                                        )
        except TimeoutException:
            reg_status = False
        assert reg_status
        driver_client.find_element(*locator.email_field).send_keys(email)
        driver_client.find_element(*locator.password_field).send_keys(password)
        button = WebDriverWait(driver_client, 5).until(EC.presence_of_element_located(locator.enter_button))
        button.click()
        try:
            auth_status = WebDriverWait(driver_client, 10).until(EC.url_to_be(url.main_page))
        except TimeoutException:
            auth_status = False
        assert auth_status

    def test_exit_from_account(self, driver_client):
        self.prepare_test_data(driver_client)
        driver_client.find_element(*locator.lk_button).click()
        WebDriverWait(driver_client, 5).until(EC.url_to_be(url.profile_page))
        driver_client.find_element(*locator.logout_button).click()
        page_status = WebDriverWait(driver_client, 5).until(EC.url_to_be(url.authorization_page))
        assert page_status
