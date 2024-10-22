from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from .forms import CustomUserCreationForm

from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('students:home')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        title = "Вы успешно прошли регистрацию!"
        message = "И мы вас с этим безумно поздравляем!"
        recipient_list = [user_email,]
        send_mail(subject=title,
                  message=message,
                  from_email=EMAIL_HOST_USER,
                  recipient_list=recipient_list)
