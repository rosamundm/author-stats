from django.contrib import admin
from django.urls import include, path
from frontend import views as frontend_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("vue", frontend_views.test_vue),
]
