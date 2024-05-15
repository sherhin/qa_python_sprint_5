import pytest

from selenium import webdriver

@pytest.fixture
def driver_client():
    """Создание вебдрайвер-клиента
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
