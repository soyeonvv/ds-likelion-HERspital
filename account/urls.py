from django.urls import path
from django.urls.conf import include
from . import views as account_views
from account.views import *
# from django.contrib.auth import views as account_views

app_name = "account"

urlpatterns = [
    path("signup/", account_views.signup, name="signup"),

    path("login/", account_views.login_view, name="login"),

    path("logout/", account_views.logout_view, name="logout"),

    path("mypage/", account_views.mypage, name="mypage"),
    
    path("setting/", account_views.setting, name="setting"),

    path("userDelete/", account_views.userDelete, name="userDelete"),

    path("update2/<str:id>", update2, name="update2"),
]