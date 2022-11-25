from django.urls import path
from .views import login_page, registration_page, Game, registrationtogame, Hello

urlpatterns = [
    path("", login_page, name="login_page"),
    path("registration", registration_page, name="registration_page"),
    path("game", Game, name="Game"),
    path("registrationtogame", registrationtogame, name="registration_page"),
    path("hello", Hello, name="Hello"),
]
