from django.urls import path
from . import views as core_views

app_name = "core"

urlpatterns = [
    path("mainpage/", core_views.mainpage, name="mainpage"),
]
