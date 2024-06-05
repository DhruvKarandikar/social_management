import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from social_user_management.custom_helpers.status_code import get_response, generic_error_2
from social_user_management.custom_helpers.model_serializers_helpers import CustomExceptionHandler
from social_user_management.serializers.user_get_serializers import UserFriendSerializerReponseApr, UserFriendSerializerRequestApr,\
        UserFriendAcceptResponseSerializer, UserFriendListSeriailizer
from social_user_management.services.user_get_service import user_friend_list_service, user_friend_apr_service
from social_user_management.custom_helpers.custom_decorator import custom_api_view

logger = logging.getLogger("django")

@csrf_exempt
@custom_api_view(
    request_serializer=UserFriendListSeriailizer,
    responses={"200": UserFriendAcceptResponseSerializer},
    operation_id="Get User Friend List"
)
def user_get_list(request):
    response_obj = None

    try:
        logger.info(request, "request for User Friend List")
        response_obj = user_friend_list_service(request)

    except CustomExceptionHandler as e:
        logger.exception(f"Custom Exception in User Friend List url: {e}")
        response_obj = get_response(eval(str(e)))

    except Exception as e:
        logger.exception(f"Exception in User Friend List url {e}")
        response_obj = get_response(generic_error_2)

    logger.info("response in User Friend List --> %s", response_obj)
    return JsonResponse(response_obj, safe=False)


@csrf_exempt
@swagger_auto_schema(
    methods=['post'],
    request_body= UserFriendSerializerRequestApr,
    responses={"200": UserFriendSerializerReponseApr},
    operation_id="User Friends A/P/R"
)
@api_view(["POST"])
def user_friend_apr(request):
    response_obj = None

    try:
        logger.debug(f"{request}, request for user sign in")
        response_obj = user_friend_apr_service(request)

    except CustomExceptionHandler as e:
        logger.exception(f"Custom Exception in user signin url: {e}")
        response_obj = get_response(eval(str(e)))

    except Exception as e:
        logger.exception(f"Exception in user signin url {e}")
        response_obj = get_response(generic_error_2)

    logger.info("response in user signin --> %s", response_obj)
    return JsonResponse(response_obj, safe=False)

