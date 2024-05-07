import random
from dataclasses import dataclass
from faker import Faker

@dataclass
class Urls:
    main_page = 'https://stellarburgers.nomoreparties.site/'
    authorization_page = main_page + 'login'
    registry_page = main_page + 'register'
    forgot_passwod_page = main_page + 'forgot-password'
    feed_page = main_page + 'feed'


@dataclass
class Selectors:
    lk_button = "//a[.='Личный Кабинет']"
    registration_button = '/html/body/div/div/main/div/div/p[1]/a'
    email_button = './/label[text() = "Email"]/../input'
    password_button = './/label[text() = "Пароль"]/../input'
    name_button = './/label[text() = "Имя"]/../input'
    registry_button = '/html/body/div/div/main/div/form/button'
    enter_button = '//main//button'

@dataclass
class Credetionals:

    login = 'tevmenova'
    password = '123456'

    def unique_email(self):
        return f'{self.login}8{random.randint(100, 999)}@yandex.ru'
