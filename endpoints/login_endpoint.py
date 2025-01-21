from endpoints.base_endpoint import BaseEndpoint
import allure


class LoginEndpoint(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self.endpoint_url = self.base_endpoint_url + '/InternalLogin'

    def login(self, data):
        with allure.step('Authorisation attempt'):
            self.post_request(self.endpoint_url, data)
        self.parse_json()

    def create_login_data(self, user_email, user_password):
        return {
            "state": "Internal",
            "username": user_email,
            "password": user_password
        }

    def check_auth_token(self):
        with allure.step('Checking accessToken after authorization attempt'):
            assert len(self.response_json['accessToken']) > 0, \
                f"Authorization failed. AccessToken is {self.response_json['accessToken']}"

    def check_response_text(self, text):
        with allure.step('Checking response text'):
            assert self.response.text == text, f'Response text ({self.response.text}) does not match {text}'
