import random
from dataclasses import dataclass

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
    registration_button = '//a[@href="/register"]' #Регистрация
    email_button = './/label[text() = "Email"]/../input' #Поле ввода email
    password_button = './/label[text() = "Пароль"]/../input' #Поле ввода пароля
    name_button = './/label[text() = "Имя"]/../input' #Поле ввода логина
    registry_button = '//button[.="Зарегистрироваться"]' #Кнопка Зарегистрироваться
    enter_button = '//main//button' #Кнопка Войти
    account_button = '//button[.="Войти в аккаунт"]' #Кнопка Войти в аккаунт
    logout_button = '//button[.="Выход"]' #Кнопка Выход
    forgot_password_auth_button = '//a[@href="/login"]' #Кнопка восстановления пароля
    constructor = ('//p[.="Конструктор"]') #Конструктор
    sauces = '//div[.="Соусы"]' #Раздел соусов
    buns = '//div[.="Булки"]' #Раздел булок
    ingredients = '//div[.="Начинки"]' #Раздел начинок
    logo_button = "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']" #Логотип



@dataclass
class Credetionals:

    login = 'tevmenova'
    password = '123456'

    def unique_email(self):
        return f'{self.login}8{random.randint(1000, 9999)}@yandex.ru'
