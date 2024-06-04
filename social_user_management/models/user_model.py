from django.db import models
from social_user_management.custom_helpers.model_serializers_helpers import AddCommonField
import uuid

class CommonUserModel(AddCommonField):

    id = models.BigAutoField(primary_key=True)
    uuid_user = models.TextField(null=False, unique=True)
    username = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email_id = models.TextField(null=False)
    password_hash = models.TextField(null=False)
    gender =models.IntegerField(null=False)

    class Meta:
        abstract = True


class UserModel(CommonUserModel):
    
    class Meta:
        db_table = "sm_user_model"
        ordering = ('-creation_date',)

