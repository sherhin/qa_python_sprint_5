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
    profile_page = main_page + 'account/profile'


@dataclass
class Selectors:
    lk_button = "//a[.='Личный Кабинет']" #Личный кабинет
    registration_button = '//a[@href="/register"]'
    email_button = './/label[text() = "Email"]/../input'
    password_button = './/label[text() = "Пароль"]/../input'
    name_button = './/label[text() = "Имя"]/../input'
    registry_button = '//button[.="Зарегистрироваться"]'
    enter_button = '//main//button'
    account_button = '//button[.="Войти в аккаунт"]'
    logout_button = '//button[.="Выход"]'
    forgot_password_auth_button = '//a[@href="/login"]'
    constructor = ('//p[.="Конструктор"]')
    sauces = '//div[.="Соусы"]'
    buns = '//div[.="Булки"]'
    ingredients = '//div[.="Начинки"]'
    logo_button = "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']"



@dataclass
class Credetionals:

    login = 'tevmenova'
    password = '123456'

    def unique_email(self):
        return f'{self.login}8{random.randint(1000, 9999)}@yandex.ru'
