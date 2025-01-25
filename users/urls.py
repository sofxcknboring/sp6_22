from django.urls import path

from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView

from users.views import RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "register/",
        RegisterView.as_view(template_name="register.html"),
        name="register",
    ),
]
