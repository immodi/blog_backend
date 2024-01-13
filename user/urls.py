from .views import *
from django.urls import path

urlpatterns = [
    path('user', GetUserByUserName.as_view(), name="get_user_by_id"),
    path(r'user/register', RegisterUser.as_view(), name="register_user"),
    path(r'user/get-with-token', GetUserNameWithToken.as_view(), name="get_username_with_token"),
    # path(r'user/logout', LogoutUser.as_view(), name="logout_user"),
]