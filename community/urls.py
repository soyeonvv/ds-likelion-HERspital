from django.urls import path
from . import views as community_views
from community.views import *

app_name = "community"

urlpatterns = [
    # path("detail/", community_views.detail, name="detail"),//
    path("communityList/", community_views.communityList, name="communityList"),
    path("expertList/", community_views.expertList, name="expertList"),
    path("consulting/", community_views.consulting, name="consulting"),
    path("communityWrite/", community_views.communityWrite, name="communityWrite"),
    path('detail/<str:id>', community_views.detail, name="detail"),
    path('expert_detail/<str:ex_id>', community_views.expert_detail, name="expert_detail"),
    path('create/', create, name="create"),
    path('communityedit/<str:id>',community_views.communityedit, name="communityedit"),
    path('update/<str:id>',update, name="update"),
]