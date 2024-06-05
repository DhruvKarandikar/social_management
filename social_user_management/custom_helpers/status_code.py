from social_user_management.custom_helpers.consts import *


success = {STATUS_CODE: SUCCESS_CODE, MESSAGE: "Success"}

generic_error_1 = {STATUS_CODE: int(f"2110000"), MESSAGE: "Invalid request details"}
generic_error_2 = {STATUS_CODE: int(f"2110001"), MESSAGE: "Please try again after sometime"}
generic_error_3 = {STATUS_CODE: int(f"2110002"), MESSAGE: "Json Data invalid"}
generic_error_4 = {STATUS_CODE: int(f"2110003"), MESSAGE: "Not authorized to access this data"}

def invalid_log_model(table_name):
    return {
        STATUS_CODE: 2100021,
        MESSAGE: f'Invalid log model initialized for model {table_name}',
    }

def obj_not_found(id,model):
    return {'status_code': 2110022, 'message': f'id = {id} not exist in {model}'}

def error_in_serializer(serializer_name):
    return {'status_code': 2110023, 'message': f'error in serializer {serializer_name}'}

def get_response(status_attribute, data=None):
    if data is None:
        return {'status': status_attribute['status_code'], 'message': status_attribute['message']}
    else:
        return {'status': status_attribute['status_code'], 'message': status_attribute['message'], 'data': data}



# Error Codes
class ErrorClass:

    gender_incorrect = {STATUS_CODE: 2110021, MESSAGE: "Enter the correct gender"}
    email_id_incorrect = {STATUS_CODE: 2110022, MESSAGE: "Enter the correct email address"}
    username_exists = {STATUS_CODE: 2110023, MESSAGE: "Username already exists"}
    email_exists = {STATUS_CODE: 2110024, MESSAGE: "Email already exists"}
    invalid_valid_credentials = {STATUS_CODE: 2110025, MESSAGE: "Either email address or password is incorrect"}
    uuid_user_none = {STATUS_CODE: 2110026, MESSAGE: "uuid user value cannot be empty"}
    uuid_user_exists = {STATUS_CODE: 2110027, MESSAGE: "User already exists"}
    password_regex_error = {STATUS_CODE: 2110028, MESSAGE: "Password must be atleast 8 characters, contains only letters numbers and must atleast contain 1 small letter, 1 Capital letter and 1 number"}
    email_or_name = {STATUS_CODE: 2110029, MESSAGE: "Either Search by Email or Name"}
    state_incorrect = {STATUS_CODE: 2110030, MESSAGE: "Enter the correct state"}
    add_friends = {STATUS_CODE: 2110031, MESSAGE: "Add Friends to connect"}
    user_not_found = {STATUS_CODE: 2110032, MESSAGE: "User not exist"}
    friend_addition = {STATUS_CODE: 2110033, MESSAGE: "You can add 3 friends at once"}

