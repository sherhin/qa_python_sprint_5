import pytest
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credetionals
from data import Urls as url
from locators import Locators as locator


@pytest.fixture(scope='function')
def driver_client():
    """Создание вебдрайвер-клиента
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
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
    WebDriverWait(
        driver_client, 5).until(EC.url_to_be(url.authorization_page)
                                )
    return email, password
