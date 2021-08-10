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
    path('expertcreate/',expertcreate, name="expertcreate"),
    path('expert_edit/<str:id>',community_views.expert_edit, name="expert_edit"),
    path('expert_update/<str:id>',expert_update, name="expert_update"),
    path('community_delete/<str:id>', community_delete, name="community_delete"),
    path('expert_delete/<str:id>', expert_delete, name="expert_delete"),
    path('expertRe_create/',expertRe_create,name="expertRe_create"),
    # path('reply/', reply, name="reply"),
    path('reply_create/', reply_create, name="replycreate"),
    # path('reply_edit/<str:id>',reply_edit,name="replyedit"),
    path('reply_update/<str:id>',reply_update, name="replyupdate"),
]