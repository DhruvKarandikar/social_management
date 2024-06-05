import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from social_user_management.custom_helpers.status_code import get_response, generic_error_2
from social_user_management.custom_helpers.model_serializers_helpers import CustomExceptionHandler
from social_user_management.serializers.user_search_serializers import UserSearchRequestSerializer, UserSearchResponseSerializer
from social_user_management.services.user_search_service import user_search_service
from social_user_management.custom_helpers.custom_decorator import custom_api_view

logger = logging.getLogger("django")

@csrf_exempt
@custom_api_view(
    request_serializer=UserSearchRequestSerializer,
    responses={"200": UserSearchResponseSerializer},
    operation_id="User Search"
)
def search_user(request):
    response_obj = None

    try:
        logger.info(request, "request for User Search")
        response_obj = user_search_service(request)

    except CustomExceptionHandler as e:
        logger.exception(f"Custom Exception in User Search url: {e}")
        response_obj = get_response(eval(str(e)))

    except Exception as e:
        logger.exception(f"Exception in User Search url {e}")
        response_obj = get_response(generic_error_2)

    logger.info("response in User Search --> %s", response_obj)
    return JsonResponse(response_obj, safe=False)

