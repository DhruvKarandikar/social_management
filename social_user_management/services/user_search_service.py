from rest_framework.pagination import PageNumberPagination
from social_user_management.custom_helpers.status_code import *
from social_user_management.custom_helpers.model_serializers_helpers import CustomExceptionHandler, validate_token
from social_user_management.serializers.user_search_serializers import HeadUserSearchSerializer
from social_user_management.models import *
from social_user_management.filters.user_search_filter import UserSearchFilter

class GetUsersPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page_no"
    page_size_query_param = "page_size"


def user_search_service(request):

    token_data = validate_token(request)
    uuid_user = token_data.user_id

    paginator = GetUsersPagination()
    validated_data = request.validation_serializer.validated_data
    
    user_filter_objs = UserSearchFilter(validated_data, queryset=UserModel.objects.all().exclude(uuid_user=uuid_user)).qs

    user_response = paginator.paginate_queryset(user_filter_objs, request)
    users = HeadUserSearchSerializer(user_response, many=True)

    response_data = {
        'count': paginator.page.paginator.count,
        'next': paginator.get_next_link(),
        'previous': paginator.get_previous_link(),
        'users': [],
    }

    if users:
        response_data['users'] = users.data

        return get_response(success, data=response_data)

    return get_response(success, data=response_data)

