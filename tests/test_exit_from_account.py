from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Urls as url
from locators import Locators as locator


class TestExitFromAccount:

    def test_exit_from_account(self, driver_client, prepare_test_data):
        email, password = prepare_test_data
        driver_client.get(url.authorization_page)
        driver_client.find_element(*locator.email_field).send_keys(email)
        driver_client.find_element(*locator.password_field).send_keys(password)
        button = WebDriverWait(driver_client, 5).until(EC.presence_of_element_located(locator.enter_button))
        button.click()
        driver_client.find_element(*locator.lk_button).click()
        WebDriverWait(driver_client, 5).until(EC.url_to_be(url.profile_page))
        driver_client.find_element(*locator.logout_button).click()
        page_status = WebDriverWait(driver_client, 5).until(EC.url_to_be(url.authorization_page))
        assert page_status
