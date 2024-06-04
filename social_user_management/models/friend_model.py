from django.db import models
from social_user_management.custom_helpers.model_serializers_helpers import AddCommonField
from django.core.validators import MaxValueValidator
from social_user_management.models import UserModel


class CommonFriendModel(AddCommonField):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserModel, to_field='id', related_name="user_friend",on_delete=models.RESTRICT, null=False)
    friend_user_name = models.CharField(max_length=255, null=False)
    friend_user_uuid = models.TextField(null=False)
    friend_email_id = models.TextField(null=False)
    friend_acceptance_status = models.IntegerField(null=False, default=0)

    class Meta:
        abstract = True

class FriendModel(CommonFriendModel):
    
    class Meta:
        db_table = "sm_friend_model"
        ordering = ('-creation_date',)
