from social_user_management.custom_helpers.status_code import *
from social_user_management.custom_helpers.model_serializers_helpers import CustomExceptionHandler, create_update_model_serializer, \
    validate_token
from social_user_management.models import *


def user_friend_list_service(request):

    from social_user_management.serializers.user_get_serializers import HeadFriendSerializer

    token_data = validate_token(request)
    uuid_user = token_data.user_id

    validate_data = request.validation_serializer.validated_data
    user_object = FriendModel.objects.filter(user_uuid=uuid_user)
    friend_state = validate_data.get('friend_acceptance_status')

    if not user_object:
        raise CustomExceptionHandler(ErrorClass.user_not_found)

    if friend_state:
        user_object = user_object.filter(friend_acceptance_status=friend_state)

    if not user_object:
        raise CustomExceptionHandler(ErrorClass.add_friends)

    serialized_obj = HeadFriendSerializer(user_object, many=True).data

    return get_response(success, data=serialized_obj)


def user_friend_apr_service(request):
    from social_user_management.serializers.user_get_serializers import HeadFriendRequestSerializer

    request_data = request.data

    token_data = validate_token(request)
    uuid_user = token_data.user_id

    user_object = UserModel.objects.filter(uuid_user=uuid_user).first()
    
    instance_friend_obj = []

    friend_email = request_data.get('friend_email_id')
    friend_obj = UserModel.objects.filter(email_id=friend_email).first()

    request_data['user_id'] = user_object.id
    request_data['user_uuid'] = user_object.uuid_user
    request_data['friend_user_name'] = friend_obj.username
    request_data['friend_user_uuid'] = friend_obj.uuid_user

    if not friend_obj:
        raise CustomExceptionHandler(ErrorClass.user_not_found)    

    instance_friend_obj = create_update_model_serializer(HeadFriendRequestSerializer, request_data, additional_data={'friend_user_uuid': friend_obj.uuid_user})

    serialized_obj = HeadFriendRequestSerializer(instance_friend_obj).data
    
    return get_response(success, data=serialized_obj)

