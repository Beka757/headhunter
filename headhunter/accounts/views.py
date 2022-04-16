from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView
from .forms import MyUserRegisterForm
from django.contrib.auth import get_user_model
from app.models import Summary, Vacancy
from django.contrib.auth.views import LoginView

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
    
    
class UserDetailsView(ListView):
    model = Summary
    template_name = 'user/detail.html'
    context_object_name = 'summaries'
    ordering = ['-updated_at']
    paginate_by = 20
    paginate_orphans = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(get_user_model(), pk=self.kwargs['pk'])
        context['summaries'] = self.get_summary_objects()
        context['vacancies'] = self.get_vacancy_objects()
        
        return context
    
    def get_object(self):
        return self.request.user
    
    def get_summary_objects(self):
        return Summary.objects.filter(user=self.kwargs['pk'])
    
    def get_vacancy_objects(self):
        return Vacancy.objects.filter(user=self.kwargs['pk'])


class LoginView(LoginView):
    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.request.user.pk})

