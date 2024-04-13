import requests
import allure
import string
import random


class BaseEndpoint:

    def __init__(self):
        self.response = None
        self.response_json = None
        self.base_endpoint_url = 'http://api.calmplete.net/api'

    def check_response_code(self, code):
        with allure.step("Check the status code"):
            assert self.response.status_code == code, \
                f'Response code does not match {code} ({self.response.status_code}).'

    def post_request(self, endpoint_url, data):
        with allure.step('Send POST request'):
            self.response = requests.post(endpoint_url, json=data)

    def parse_json(self):
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            self.response_json = self.response.json()

    def create_user_email(self, email_mode):

        with allure.step('Creating fake user email'):
            character_letters = list(string.ascii_lowercase)
            character_letters_uppercase = list(string.ascii_uppercase)
            character_digits = [str(i) for i in range(0, 10)]
            character_special = list(string.punctuation)
            character_special.remove("@")
            character_special.remove("'")
            domains = ['@yahoo.com', '@google.com', '@mail.com', '@outlook.com', '@icloud.com', '@proton.me']

            email = ''
            counter = 15
            while counter > 0:
                email += random.choice(character_letters)
                counter -= 1
                if email_mode.find('upper') != -1:
                    email += random.choice(character_letters_uppercase)
                    counter -= 1

                if email_mode.find('digits') != -1:
                    email += random.choice(character_digits)
                    counter -= 1

                if email_mode.find('special') != -1:
                    email += random.choice(character_special)
                    counter -= 1

        return email + random.choice(domains)

    def create_user_password(self, pass_mode='upper,digits,special', pass_len=8):

        with allure.step('Creating fake user password'):
            character_letters = list(string.ascii_lowercase)
            character_letters_uppercase = list(string.ascii_uppercase)
            character_digits = [str(i) for i in range(0, 10)]
            character_special = list(string.punctuation)

            user_password = ''

            while pass_len > 0:
                user_password += random.choice(character_letters)
                pass_len -= 1
                if pass_len <= 0:
                    break
                if pass_mode.find('upper') != -1:
                    user_password += random.choice(character_letters_uppercase)
                    pass_len -= 1
                    if pass_len <= 0:
                        break
                if pass_mode.find('digits') != -1:
                    user_password += random.choice(character_digits)
                    pass_len -= 1
                    if pass_len <= 0:
                        break
                if pass_mode.find('special') != -1:
                    user_password += random.choice(character_special)
                    pass_len -= 1
                    if pass_len <= 0:
                        break
        return user_password


if __name__ == '__main__':
    base_obj = BaseEndpoint()
    print(base_obj.create_user_password('upper,digits,special', 7))
