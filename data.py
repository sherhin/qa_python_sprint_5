import random
from dataclasses import dataclass
from faker import Faker


WEBSITE = 'https://stellarburgers.nomoreparties.site/'

@dataclass
class Selectors:
    lk_button = "//a[.='Личный Кабинет']"
    registration_button = '/html/body/div/div/main/div/div/p[1]/a'
    email_button = './/label[text() = "Email"]/../input'
    password_button = './/label[text() = "Пароль"]/../input'
    name_button = './/label[text() = "Имя"]/../input'
    registry_button = '/html/body/div/div/main/div/form/button'
    enter_button = '/html/body/div/div/main/div/form/button'
    auth_email = '/html/body/div/div/main/div/form/fieldset[1]/div/div/label'
    auth_password = '/html/body/div/div/main/div/form/fieldset[2]/div/div'

@dataclass
class Credetionals:

    login = 'tevmenova'
    password = '123456'

    def unique_email(self):
        return f'{self.login}8{random.randint(100, 999)}@yandex.ru'
