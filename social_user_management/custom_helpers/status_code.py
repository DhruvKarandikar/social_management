from social_user_management.custom_helpers.consts import *


success = {STATUS_CODE: SUCCESS_CODE, MESSAGE: "Success"}

generic_error_1 = {STATUS_CODE: int(f"2110000"), MESSAGE: "Invalid request details"}
generic_error_2 = {STATUS_CODE: int(f"2110001"), MESSAGE: "Please try again after sometime"}

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

