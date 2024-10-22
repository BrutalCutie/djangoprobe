from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from .forms import CustomUserCreationForm

from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user)
        return super().form_valid(form)

    @staticmethod
    def send_welcome_email(user_data):
        user_email = user_data.email

        title = "Вы успешно прошли регистрацию!"
        message = "И мы вас с этим безумно поздравляем!"
        recipient_list = [user_email,]
        send_mail(subject=title,
                  message=message,
                  from_email=EMAIL_HOST_USER,
                  recipient_list=recipient_list)
