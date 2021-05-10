# 프로젝트_루트/프로젝트_이름/urls.py
# --------------------------------------------------

from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls'))

]
