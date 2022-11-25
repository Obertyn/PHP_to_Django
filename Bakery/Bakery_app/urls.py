# pages/urls.py
from django.urls import path
from .views import page1, page2

urlpatterns = [
    path("", page1, name="home"),
    path("order", page2, name="home"),
]

