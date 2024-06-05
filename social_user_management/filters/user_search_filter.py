import django_filters
import logging
from django.db.models import Q
from social_user_management.models import *

logger = logging.getLogger('django')

class UserSearchFilter(django_filters.FilterSet):

    email_id = django_filters.CharFilter(field_name='email_id', method='user_filter')
    first_name = django_filters.CharFilter(field_name='first_name', method='user_filter')

    def user_filter(self, queryset, field_name, value):

        email_id = self.data.get('email_id')
        first_name = self.data.get('first_name')

        user_queryset = queryset

        if email_id:
            user_queryset = user_queryset.filter(Q(email_id__icontains=email_id))

        if first_name:
            user_queryset = user_queryset.filter(Q(first_name__icontains=first_name))

        return user_queryset

    class Meta:
        model = UserModel
        fields = ['email_id', 'first_name']
