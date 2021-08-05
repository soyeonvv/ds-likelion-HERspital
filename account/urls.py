from django.urls import path
from . import views as account_views

app_name = "account"

urlpatterns = [
    path("signup/", account_views.signup, name="signup"),
    path("login/", account_views.login, name="login"),
    path("mypage/", account_views.mypage, name="mypage"),
    path("setting/", account_views.setting, name="setting"),
    path("stchange/", account_views.stchange, name="stchange"),
    path("stcancel/", account_views.stcancel, name="stcancel"),
    path("stdelete/", account_views.stdelete, name="stdelete"),
]