import random


class Urls:
    main_page = 'https://stellarburgers.nomoreparties.site/'
    authorization_page = main_page + 'login'
    registry_page = main_page + 'register'
    forgot_password_page = main_page + 'forgot-password'
    feed_page = main_page + 'feed'
    profile_page = main_page + 'account/profile'


class Credetionals:
    def __init__(self):
        self.login = 'tevmenova'
        self.password = '123456'
        self.email = self.unique_email(login=self.login)

    @staticmethod
    def unique_email(login):
        email = f'{login}8{random.randint(10000, 99999)}@yandex.ru'
        return email

