
from social_user_management.custom_helpers.status_code import *
from social_user_management.custom_helpers.model_serializers_helpers import CustomExceptionHandler, create_update_model_serializer, \
        salt_and_hash, generate_token_pair
from social_user_management.models import *
import uuid

def password_verification(user_object, secret):

    user_uuid = user_object.first().uuid_user
    password = user_object.first().password_hash
    user_id = user_object.first().id

    refresh_token_obj = RefreshToken.objects.filter(user_id=user_id).first()

    if password == salt_and_hash(user_uuid, secret).upper():
        access_token, refresh_token = generate_token_pair(user_object)

        if refresh_token_obj:
            refresh_token = refresh_token_obj.refresh_token
        else:
            RefreshToken.objects.create(refresh_token=refresh_token, user_id=user_id)
    else:
        raise CustomExceptionHandler(ErrorClass.invalid_valid_credentials)

    return access_token, refresh_token



def user_sign_in_service(request_data):

    from social_user_management.serializers.user_make_serializers import UserLoginRequestSerializer

    serialized_data = UserLoginRequestSerializer(data=request_data)

    if not serialized_data.is_valid():
        raise CustomExceptionHandler(generic_error_3)

    email_id = serialized_data.data.get('email_id')
    password =  serialized_data.data.get('password')

    user_obj = UserModel.objects.filter(email_id__iexact=email_id ,status=STATUS_ACTIVE)

    if len(user_obj) > 1:
        raise CustomExceptionHandler(ErrorClass.email_exists)

    access_token, refresh_token = password_verification(user_obj, password)

    return get_response(success, data={"access_token": access_token, "refresh_token": refresh_token})




def user_sign_up_service(request_data):
    
    from social_user_management.serializers.user_make_serializers import HeadUserSerializer, UserSignUpRequestSerializer

    password = request_data.get('password')

    user_uuid = uuid.uuid4()

    secret_hash = salt_and_hash(str(user_uuid), password)
    request_data['password_hash'] = secret_hash.upper()
    request_data['uuid_user'] = str(user_uuid)

    serializer_obj = create_update_model_serializer(HeadUserSerializer,request_data,partial=True)

    if serializer_obj:
        return get_response(success)

    else:
        return CustomExceptionHandler(generic_error_1)


