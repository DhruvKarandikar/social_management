from django.urls import path
from .views import *

urlpatterns = [
    # paths for user management

    path('user_management/user_signup', user_sign_up, name='user signup'),
    path('user_management/user_signin', user_sign_in, name='user signin'),
    path('user_management/user_search', search_user, name='user search'),
    path('user_management/get_user_friends_list', user_get_list, name='user friends list'),
    path('user_management/user_apr', user_friend_apr, name='user friend apr'),

]
