from django.urls import path
from .views import register_view,user_login,profile,user_logout

urlpatterns=[
    path("register/",register_view,name="register_view"),
    path("login/",user_login,name="user_login"),
    path("profile/",profile,name="profile"),
    path("logout/",user_logout,name="user_logout")
]