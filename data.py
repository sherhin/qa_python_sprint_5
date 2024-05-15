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
        self.email = self.email()

    @staticmethod
    def unique_email(login):
        email = f'{login}8{random.randint(1000, 9999)}@yandex.ru'
        return email

    def login(self):
        return self.login

    def password(self):
        return self.password

    def email(self):
        email = self.unique_email(self.login)
        return email
