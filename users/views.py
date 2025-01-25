from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def send_welcome_mail(self, user_email):
        subject = "Welcome buddy!"
        message = "Registarion complete!"
        from_email = EMAIL_HOST_USER
        recipient_list = [
            user_email,
        ]
        send_mail(subject, message, from_email, recipient_list)
