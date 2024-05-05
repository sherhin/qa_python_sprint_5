import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Selectors as selector
from data import Credetionals as cred

from data import Selectors


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выберите браузер: (chrome/firefox)")


@pytest.fixture(scope='class')
def driver_client(request):
    """Создание вебдрайвер-клиента
    """
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser option")
    time.sleep(5)
    yield driver
    time.sleep(10)
    driver.quit()

@pytest.fixture(scope='class')
def delete_all_cookies(driver_client):
    driver_client.delete_all_cookies()

@pytest.fixture()
def browser_helper(driver_client):
    """Создание экземпляра класса хэлпера
    """
    browser_helper = BrowserHelpers(driver_client)
    return browser_helper


class BrowserHelpers():
    """ Класс с общими методами для взаимодействия с сайтом.
    """

    def __init__(self, driver_client):
        self.driver = driver_client

    def get_page(self, url: str):
        """ Переход по url
        """
        logging.info(f'Переходим на страницу: {url}')
        self.driver.get(url)

    def get_current_page(self):
        current_url = self.driver.current_url
        return current_url

    def click_button(self, button):
        button.click()

    def get_personal_account_page(self, driver_client, website):
        self.get_page(website)
        lk_button = selector.lk_button
        driver_client.find_element(By.XPATH, lk_button).click()
        current_url = self.get_current_page()
        return 'login' in current_url

    def get_registration_page(self, driver_client, website):
        self.get_personal_account_page(driver_client, website)
        registration_button = selector.registration_button
        driver_client.find_element(By.XPATH, registration_button).click()
        current_url = self.get_current_page()
        return 'register' in current_url

    def registration(
            self, driver_client, website, reg_login,
            reg_email, reg_password
    ):
        self.get_registration_page(driver_client, website)
        email = selector.email_button
        password = selector.password_button
        login = selector.name_button
        registry_button = selector.registry_button
        email_field = driver_client.find_element(By.XPATH, email)
        login_field = driver_client.find_element(By.XPATH, login)
        password_field = driver_client.find_element(By.XPATH, password)
        email_field.send_keys(reg_email)
        login_field.send_keys(reg_login)
        password_field.send_keys(reg_password)
        driver_client.find_element(By.XPATH, registry_button).click()
        current_url = self.get_current_page()
        return 'login' in current_url, reg_email, reg_password

    # def clear_input_field(self, locator_path: str) -> None:
    #     """ Очищает input поле ввода
    #     """
    #     while len(self.driver.xpath(locator_path).attr('value')) != 0:
    #         self.driver.xpath(locator_path).send_keys(Keys.CONTROL + "a")
    #         self.driver.xpath(locator_path).send_keys(Keys.DELETE)
    #
    # def send_keys(self, locator_path: str, value: str):
    #     """ Очищает поле ввода и вводит в него переданное значение
    #     """
    #     self.clear_input_field(locator_path)
    #     self.driver.xpath(locator_path).send_keys(value)

# # class FixturesForUI(pytest, selector):
# #     @classmethod
# #     def browser(self):
# #         driver = webdriver.Chrome()
# #         yield driver
# #         driver.quit()
# #
# #     def personal_account_page():
# #         cls.browser.get(WEBSITE)
# #         lk_button = browser.find_element(By.XPATH, selector.get('lk_button'))
# #         lk_button.click()
# #
# #     @staticmethod
# #     def get_current_url(browser):
# #         current_url = browser.current_url
# #         return current_url
