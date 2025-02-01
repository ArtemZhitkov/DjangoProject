import secrets
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm, CustomUserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from config.settings import EMAIL_HOST_USER
from .models import CustomUser


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False  # Ставим флаг активности на False для пользователя до подтверждения регистрации
        self.send_verification_email(user)  # Отправка подтверждения регистрации
        self.send_welcome_email(user.email)  # Отправка электронного письма с приветствием
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        # Отправка электронного письма с приветствием
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

    def send_verification_email(self, user):
        # Отправка подтверждения регистрации
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение регистрации',
            message=f'Для подтверждения регистрации перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email, ]
        )

def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserEditForm
    template_name = 'users/profile_edit.html'
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy('users:profile_detail')
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('users:profile_detail', kwargs={'pk': self.kwargs['pk']})

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile_detail.html'
    login_url = reverse_lazy("users:login")
    context_object_name = 'user'

