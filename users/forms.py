from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "avatar",
            "email",
            "country",
            "phone",
            "password1",
            "password2",
        ]
