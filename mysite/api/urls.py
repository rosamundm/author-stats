from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# register viewset with router class for automatic URL generation:
router.register(r"book-api", views.BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
