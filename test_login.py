from endpoints.login_endpoint import LoginEndpoint
from endpoints.registration_endpoint import RegistrationEndpoint
import allure

@allure.feature('User login feature')
def test_login_email_password_registered_email_and_password_successful():

    registration_obj = RegistrationEndpoint()
    reg_data = registration_obj.create_reg_data()
    registration_obj.register_user(reg_data)

    login_obj = LoginEndpoint()
    login_data = login_obj.create_login_data(reg_data['email'], reg_data['password'])
    login_obj.login(login_data)

    login_obj.check_response_code(200)
    login_obj.check_auth_token()

def test_login_email_password_registered_email_invalid_password_fail():
    registration_obj = RegistrationEndpoint()
    reg_data = registration_obj.create_reg_data()
    registration_obj.register_user(reg_data)

    login_obj = LoginEndpoint()
    login_data = login_obj.create_login_data(reg_data['email'], login_obj.create_user_password())

    login_obj.login(login_data)

    login_obj.check_response_code(400)
    login_obj.check_response_text('Error while authorizing user.')



