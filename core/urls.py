from django.urls import path
from . import views as core_views
from django.conf import settings
from django.conf.urls.static import static
from core.views import *

app_name = "core"

urlpatterns = [
    path("mainpage/", core_views.mainpage, name="mainpage"),
    path("create_review", core_views.create_review, name="create_review"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
