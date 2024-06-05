from rest_framework import serializers
from django.db.models import Q
from social_user_management.models import *
from django.db.transaction import atomic
from social_user_management.custom_helpers.model_serializers_helpers import dict_get_key_from_value, help_text_for_dict \
    , CustomExceptionHandler, comman_create_update_services, common_checking_and_passing_value_from_list_dict
from social_user_management.custom_helpers.consts import *
from social_user_management.custom_helpers.status_code import *


class HeadUserSearchSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    email_id = serializers.CharField(required=True)
    gender = serializers.CharField(required=True, help_text=help_text_for_dict(gender_dict))

    class Meta:
        model = UserModel
        fields = ("username", "first_name", "last_name", "email_id", "gender",)

    def validate(self, data):
        data = super().validate(data)
        return {key: value for key, value in data.items() if value is not None}
    
    def to_representation(self, data):
        data = super().to_representation(data)

        if data.get('gender'):
            data['gender'] = dict_get_key_from_value(gender_dict, data['gender'])

        return data 


class UserSearchRequestSerializer(serializers.Serializer):

    email_id = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)

    class Meta:
        model = UserModel
        fields = ("email_id", "first_name",)

    def validate(self, data):
        data = super().validate(data)

        email = data.get('email')
        first_name = data.get('first_name')

        if email and first_name:
            raise CustomExceptionHandler(ErrorClass.email_or_name)

        return data


class PaginateSerializer(serializers.Serializer):
    count = serializers.IntegerField(required=False)
    next = serializers.CharField(required=False)
    previous = serializers.CharField(required=False)
    users = HeadUserSearchSerializer(required=False, many=True)


class UserSearchResponseSerializer(serializers.Serializer):

    status = serializers.IntegerField(required=False)
    message = serializers.CharField(required=False)
    data = PaginateSerializer(required=False)

    class Meta:
        model = UserModel
        fields = ('status','message', 'data',)

