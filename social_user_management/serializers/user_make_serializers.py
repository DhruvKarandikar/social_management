from rest_framework import serializers
from django.db.models import Q
from social_user_management.models import *
from django.db.transaction import atomic
from social_user_management.custom_helpers.model_serializers_helpers import dict_get_key_from_value, help_text_for_dict \
    , CustomExceptionHandler, comman_create_update_services, common_checking_and_passing_value_from_list_dict
from social_user_management.custom_helpers.consts import *
import re
from social_user_management.custom_helpers.status_code import *

def password_regex(password):  

    if len(password) < 8:
        raise False
    if not re.search("[a-z]", password):
        raise False
    if not re.search("[A-Z]", password):
        raise False
    if not re.search("[0-9]", password):
        return False
    return True


class HeadUserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=255, required=True)
    uuid_user = serializers.CharField(required=True)
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    email_id = serializers.CharField(required=True)
    password_hash = serializers.CharField(required=True)
    gender = serializers.CharField(required=True, help_text=help_text_for_dict(gender_dict))

    class Meta:
        model = UserModel
        exclude = ("status", "creation_date", "creation_by", "updation_date", "updation_by",)

    def validate_gender(self,value):
        return common_checking_and_passing_value_from_list_dict(value, gender_dict, ErrorClass.gender_incorrect)

    def validate_email_id(self,value):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  
        if not re.fullmatch(regex, value):
            raise CustomExceptionHandler(ErrorClass.email_id_incorrect)  
        return value

    def validate_password(self,value):

        if value:
            bool_regex = password_regex(value)

            if bool_regex == False:
                raise CustomExceptionHandler(ErrorClass.password_regex_error)

        return value

    def validate_uuid_user(self, value):
        if value in [None, "", 0]:
            raise CustomExceptionHandler(ErrorClass.uuid_user_none)

        if UserModel.objects.filter(uuid_user__iexact=value).exists():
            raise CustomExceptionHandler(ErrorClass.uuid_user_exists)

        return value

    def validate_username(self,value):
        if UserModel.objects.filter(username__iexact=value).exists():
            raise CustomExceptionHandler(ErrorClass.username_exists)
        return value

    def validate(self, data):
        data = super().validate(data)
        return {key: value for key, value in data.items() if value is not None}

    @atomic
    def create(self, validated_data):
        return comman_create_update_services(self, validated_data)

    def to_representation(self, data):
        data = super().to_representation(data)

        if data.get('gender'):
            data['gender'] = dict_get_key_from_value(gender_dict, data['gender'])

        return data 

# User Sign up Serializer 

class UserSignUpRequestSerializer(HeadUserSerializer):
    password = serializers.CharField(required=True)
    password_hash = None
    uuid_user = None

    class Meta:
        model = UserModel
        exclude = ("status", "creation_date", "creation_by", "updation_date", "updation_by", "password_hash","uuid_user")

class UserSignUpResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField(required=False)
    message = serializers.CharField(required=False)

    class Meta:
        model = UserModel
        fields = ('status','message',)

# User Signin Serializer

class UserLoginRequestSerializer(HeadUserSerializer):

    email_id = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = UserModel
        fields = ('email_id','password',)


class SigninDataResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=False)
    refresh_token = serializers.CharField(required=False)
    
    class Meta:
        model = RefreshToken
        fields = ("access_token", "refresh_token",)


class UserLoginResponseSerializers(serializers.Serializer):
    status = serializers.IntegerField(required=False)
    message = serializers.CharField(required=False)
    data = SigninDataResponseSerializer(required=False)

    class Meta:
        model = UserModel
        fields = ('status','message', 'data',)

