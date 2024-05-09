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

    def test_account_button_logout_is_clickable(self, driver_client, browser_helper):
        personal_account_page = browser_helper.get_personal_account_page(driver_client)
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

    def test_authorization(self, browser_helper, driver_client):
        email = cred().unique_email()
        registry_status, email, password = browser_helper.registration(
            driver_client, cred.login, email, cred.password
        )
        if registry_status:
            auth_status = browser_helper.authorization(driver_client, email, password)
            assert auth_status

    def test_logout(self,browser_helper, driver_client):
        email = cred().unique_email()
        registry_status, email, password = browser_helper.registration(
            driver_client, cred.login, email, cred.password
        )
        if registry_status:
            browser_helper.authorization(driver_client, email, password)
        '''Тут разлогин дописать'''


