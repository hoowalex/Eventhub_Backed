from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout_view", views.logout_view, name="logout_view"),
]