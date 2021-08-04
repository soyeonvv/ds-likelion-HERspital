from django.urls import path
from . import views as community_views

app_name = "community"

urlpatterns = [
    path("detail/", community_views.detail, name="detail"),
    path("communityList/", community_views.communityList, name="communityList"),
    path("expertList/", community_views.expertList, name="expertList"),
    path("consulting/", community_views.consulting, name="consulting"),
]