from rest_framework import serializers
from django.db.models import Q
from social_user_management.models import *
from django.db.transaction import atomic
from social_user_management.custom_helpers.model_serializers_helpers import dict_get_key_from_value, help_text_for_dict \
    , CustomExceptionHandler, comman_create_update_services, common_checking_and_passing_value_from_list_dict
from social_user_management.custom_helpers.consts import *
from social_user_management.custom_helpers.status_code import *

class HeadFriendSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(required=False)
    friend_user_name = serializers.CharField(required=False)
    friend_email_id = serializers.CharField(required=False)
    user_uuid = serializers.CharField(required=False)
    friend_acceptance_status = serializers.CharField(required=False, help_text=help_text_for_dict(friend_acceptance_state))

    class Meta:
        model = FriendModel
        fields = ("id", "user_id", "user_uuid", "friend_user_name", "friend_email_id", "friend_acceptance_status",) 

    @atomic
    def create(self, validated_data):
        return comman_create_update_services(self, validated_data)

    def validate_friend_acceptance_status(self, value):
        return common_checking_and_passing_value_from_list_dict(value, friend_acceptance_state, ErrorClass.state_incorrect)

    def to_representation(self, data):
        data = super().to_representation(data)

        if data.get('friend_acceptance_status'):
            data['friend_acceptance_status'] = dict_get_key_from_value(friend_acceptance_state, data['friend_acceptance_status'])

        return data 


# APR Serializer Friend
class HeadFriendRequestSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField(required=False)
    friend_user_name = serializers.CharField(required=False)
    friend_email_id = serializers.CharField(required=False)
    friend_acceptance_status = serializers.CharField(required=False, help_text=help_text_for_dict(friend_acceptance_state))

    class Meta:
        model = FriendModel
        fields = ("user_id", "friend_user_name", "friend_email_id", "friend_acceptance_status",) 
    
    @atomic
    def create(self, validated_data):
        return comman_create_update_services(self, validated_data)

    def validate_friend_acceptance_status(self, value):
        return common_checking_and_passing_value_from_list_dict(value, friend_acceptance_state, ErrorClass.state_incorrect)

    def to_representation(self, data):
        data = super().to_representation(data)

        if data.get('friend_acceptance_status'):
            data['friend_acceptance_status'] = dict_get_key_from_value(friend_acceptance_state, data['friend_acceptance_status'])

        return data
    

class UserFriendSerializerRequestApr(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    friend_email_id = serializers.CharField(required=True)
    friend_acceptance_status = serializers.CharField(required=True, help_text=help_text_for_dict(friend_acceptance_state))

    class Meta:
        model = FriendModel
        fields = ("id","friend_email_id", "friend_acceptance_status",)


class UserFriendSerializerReponseApr(serializers.Serializer):

    status = serializers.IntegerField(required=False)
    message = serializers.CharField(required=False)
    data = HeadFriendSerializer(required=False)

    class Meta:
        model = FriendModel
        fields = ('status','message', 'data',)


# user friend list serializer

class UserFriendListSeriailizer(serializers.ModelSerializer):

    friend_acceptance_status = serializers.CharField(required=False, help_text=help_text_for_dict(friend_acceptance_state))
    
    class Meta:
        model = FriendModel
        fields = ("friend_acceptance_status",)

    def validate_friend_acceptance_status(self, value):
        return common_checking_and_passing_value_from_list_dict(value, friend_acceptance_state, ErrorClass.state_incorrect)

    def to_representation(self, data):
        data = super().to_representation(data)

        if data.get('friend_acceptance_status'):
            data['friend_acceptance_status'] = dict_get_key_from_value(friend_acceptance_state, data['friend_acceptance_status'])

        return data

class UserFriendAcceptResponseSerializer(serializers.Serializer):

    status = serializers.IntegerField(required=False)
    message = serializers.CharField(required=False)
    data = HeadFriendSerializer(required=False, many=True)

    class Meta:
        model = FriendModel
        fields = ('status','message', 'data',)

