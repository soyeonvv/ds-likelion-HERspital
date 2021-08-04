from django.urls import path
from . import views as community_views

app_name = "community"

urlpatterns = [
    path("detail/", community_views.detail, name="detail"),
]