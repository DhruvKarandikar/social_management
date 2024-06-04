from django.urls import path
from .views import *

urlpatterns = [
    # paths for user management

    path('user_management/user_signup', user_sign_up, name='user signup'),
    path('user_management/user_signin', user_sign_in, name='user signin'),

]
