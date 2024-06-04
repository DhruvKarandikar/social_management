from django.db import models
from social_user_management.models import UserModel

class RefreshToken(models.Model):
    refresh_token = models.TextField(primary_key=True)
    user = models.ForeignKey(UserModel, to_field='id', related_name='refresh_user', on_delete=models.RESTRICT, null=False)
