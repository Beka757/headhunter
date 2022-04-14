from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from .forms import MyUserRegisterForm
from django.contrib.auth import login, get_user_model

# Create your views here.


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'registration/register.html'
    form_class = MyUserRegisterForm

    def form_valid(self, form):
        user = form.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('login')

