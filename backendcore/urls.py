from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backendcore.views import TodoViewSet, RegisterAPI, LoginAPI
from . import views

from knox import views as knox_views

# from .views import LoginAPI
from django.urls import path

router = DefaultRouter()
# router.register(r"todos", TodoViewSet)
router.register("todos", views.TodoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/register/", RegisterAPI.as_view(), name="register"),
    path("api/login/", LoginAPI.as_view(), name="login"),
    path("api/logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("api/logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
]
