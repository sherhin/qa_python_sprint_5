import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from data import Selectors as selector
from data import Urls as url
from selenium.webdriver.support.wait import WebDriverWait

from data import Credetionals as cred



WEBSITE = 'https://stellarburgers.nomoreparties.site/'



@pytest.mark.usefixtures('driver_client', 'delete_all_cookies')
class TestRegistration:
    #
    # def test_account_button_logout_is_clickable(self, driver_client, browser_helper):
    #     personal_account_page = browser_helper.get_personal_account_page(driver_client)
    #     assert personal_account_page == url.authorization_page
    #
    # def test_registration_button_is_clickable(self, driver_client, browser_helper):
    #     registry_page = browser_helper.get_registration_page(driver_client)
    #     assert registry_page == url.registry_page
    #
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
    # def test_authorization(self, browser_helper, driver_client):
    #     cred.email = cred().unique_email()
    #     registry_status, email, password = browser_helper.registration(
    #         driver_client, WEBSITE, cred.login, cred.email, cred.password
    #     )
    #     WebDriverWait(driver_client, 10).until(expected_conditions.url_contains('login'))
    #     email_field = selector.email_button
    #     password_field = selector.password_button
    #     enter_button = selector.enter_button
    #     driver_client.find_element(By.XPATH, email_field).send_keys(email)
    #     driver_client.find_element(By.XPATH, password_field).send_keys(password)
    #     driver_client.find_element(By.XPATH, enter_button).click()
    #


    # def test_email_form(self, driver_client, browser_helper):
    #     browser_helper.get_personal_account_page(driver_client, WEBSITE)
    #     email_field = selector.email_button
    #     driver_client.find_element(By.XPATH, email_field).send_keys('yandex')
    #     time.sleep(10)

    # def test_password_form(self, driver_client, browser_helper):
    #     browser_helper.get_personal_account_page(driver_client, WEBSITE)
    #     password_field = selector.password_button
    #     driver_client.find_element(By.XPATH, password_field).send_keys('yandex')
    #     time.sleep(10)
    # name_input = browser.find_element(By.ID,)
    # password_input =
    # submit_button =
    # assert "Регистрация прошла успешно" in browser.page_source

# def test_invalid_password(browser):
#     browser.get("https://www.example.com")
#     # Здесь должен быть код для регистрации с недопустимым паролем
#     assert "Пароль должен содержать не менее 8 символов" in browser.page_source
