from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Urls as url
from locators import Locators as locator


class TestAuthorization:

    def test_authorization_from_main_page(self, driver_client, prepare_test_data):
        email, password = prepare_test_data
        driver_client.get(url.main_page)
        driver_client.find_element(*locator.account_button).click()
        WebDriverWait(driver_client, 5).until(EC.url_to_be(url.authorization_page))
        driver_client.find_element(*locator.email_field).send_keys(email)
        driver_client.find_element(*locator.password_field).send_keys(password)
        button_to_click = WebDriverWait(driver_client, 5).until(EC.presence_of_element_located(locator.enter_button))
        button_to_click.click()
        auth_status = WebDriverWait(driver_client, 10).until(EC.url_to_be(url.main_page))
        assert auth_status

    def test_authorization_from_authorization_page(self, driver_client, prepare_test_data):
        email, password = prepare_test_data
        driver_client.get(url.authorization_page)
        driver_client.find_element(*locator.email_field).send_keys(email)
        driver_client.find_element(*locator.password_field).send_keys(password)
        button_to_click = WebDriverWait(driver_client, 5).until(EC.presence_of_element_located(locator.enter_button))
        button_to_click.click()
        auth_status = WebDriverWait(driver_client, 10).until(EC.url_to_be(url.main_page))
        assert auth_status

    def test_authorization_from_forgot_password_page(self, driver_client, prepare_test_data):
        email, password = prepare_test_data
        driver_client.get(url.forgot_password_page)
        driver_client.find_element(*locator.lk_button).click()
        driver_client.find_element(*locator.email_field).send_keys(email)
        driver_client.find_element(*locator.password_field).send_keys(password)
        button_to_click = WebDriverWait(driver_client, 5).until(EC.presence_of_element_located(locator.enter_button))
        button_to_click.click()
        auth_status = WebDriverWait(driver_client, 10).until(EC.url_to_be(url.main_page))
        assert auth_status
