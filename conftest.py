
import pytest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from data import Urls as url
from data import Selectors as selector
from data import Credetionals as cred



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
    yield driver
    driver.quit()

@pytest.fixture
def driver_incognito(request):
    """Создание инкогнито вебдрайвер-клиента
    """
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--incognito")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError("Unsupported browser option")
    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver

@pytest.fixture(scope='class')
def authorize(driver_client):
    """ Фикстура авторизации
    """
    browser_helper = BrowserHelpers(driver_client)
    email = cred().unique_email()
    registry_status, email, password = browser_helper.registration(
        driver_client, cred.login, email, cred.password
    )
    browser_helper.authorization(driver_client, email, password)

@pytest.fixture(scope='class')
def delete_all_cookies(driver_client):
    """ Фикстура очистки куков
    """
    driver_client.delete_all_cookies()



@pytest.fixture
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
        self.wait_client(driver_client)

    def get_page(self, url: str):
        """ Переход по url
        """
        self.driver.get(url)

    def get_current_page(self):
        current_url = self.driver.current_url
        return current_url

    def click_button(self, button):
        button.click()

    def wait_client(self, driver_client, timeout=5):
        wait_client = WebDriverWait(driver_client, timeout)
        return wait_client

    def wait_element_is_presence(self, driver_client, element):
        self.wait_client(driver_client, timeout=10).until(EC.presence_of_element_located(element))
        return driver_client.find_element(*element)


    def get_personal_account_page_logout(self, driver_client):
        self.get_page(url.main_page)
        lk_button = selector.lk_button
        driver_client.find_element(By.XPATH, lk_button).click()
        try:
            page_status = self.wait_client(driver_client).until(EC.url_to_be(url.authorization_page))
        except TimeoutException:
            page_status = False
        return page_status

    def get_profile_page(self, driver_client):
        self.get_page(url.main_page)
        lk_button = selector.lk_button
        driver_client.find_element(By.XPATH, lk_button).click()
        try:
            page_status = self.wait_client(driver_client).until(EC.url_to_be(url.profile_page))
        except TimeoutException:
            page_status = False
        return page_status

    def logout(self, driver_client):
        self.get_profile_page(driver_client)
        logout_button = selector.logout_button
        find_button = (By.XPATH, logout_button)
        button_to_click = self.wait_element_is_presence(driver_client, find_button)
        button_to_click.click()
        try:
            page_status = self.wait_client(driver_client).until(EC.url_to_be(url.authorization_page))
        except TimeoutException:
            page_status = False
        return page_status

    def get_registration_page(self, driver_client):
        driver_client.get(url.authorization_page)
        registration_button = selector.registration_button
        reg_button = (By.XPATH, registration_button)
        button_to_click = self.wait_element_is_presence(driver_client, reg_button)
        button_to_click.click()
        self.wait_client(driver_client).until(EC.url_to_be(url.registry_page))
        try:
            page_status = self.wait_client(driver_client).until(EC.url_to_be(url.registry_page))
        except TimeoutException:
            page_status = False
        return page_status

    def registration(
            self, driver_client, reg_login,
            reg_email, reg_password
    ):
        driver_client.get(url.registry_page)
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
        if len(reg_password) < 6:
            error_element = driver_client.find_element(By.CLASS_NAME, "input__error")
            assert error_element
        try:
            reg_status = self.wait_client(driver_client).until(EC.url_to_be(url.authorization_page))
        except TimeoutException:
            reg_status = False
        return reg_status, reg_email, reg_password

    def authorization(self, driver_client, email, password, from_page=url.authorization_page):
        auth_button = str
        driver_client.get(from_page)
        if from_page == url.main_page:
            auth_button = selector.account_button
        elif from_page == url.authorization_page:
            auth_button = selector.lk_button
        elif from_page == url.forgot_passwod_page:
            auth_button = selector.forgot_password_auth_button

        driver_client.find_element(By.XPATH, auth_button).click()
        email_field = selector.email_button
        password_field = selector.password_button
        enter_button = selector.enter_button
        driver_client.find_element(By.XPATH, email_field).send_keys(email)
        driver_client.find_element(By.XPATH, password_field).send_keys(password)
        ent_button = (By.XPATH, enter_button)
        button_to_click = self.wait_element_is_presence(driver_client, ent_button)
        button_to_click.click()
        try:
            auth_status = self.wait_client(driver_client).until(EC.url_to_be(url.main_page))
        except TimeoutException:
            auth_status = False
        return auth_status


