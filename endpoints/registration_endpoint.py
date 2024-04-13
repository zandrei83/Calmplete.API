from .base_endpoint import BaseEndpoint
import allure


class RegistrationEndpoint(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self.endpoint_url = self.base_endpoint_url + '/InternalLogin/sign-up'

    def create_reg_data(self, email_mode='', pass_mode='upper,digits,special', pass_len=8):
        return {
            "email": self.create_user_email(email_mode),
            "password": self.create_user_password(pass_mode, pass_len)
        }

    def register_user(self, data):
        with allure.step('Creating new user'):
            self.post_request(self.endpoint_url, data)
        self.parse_json()