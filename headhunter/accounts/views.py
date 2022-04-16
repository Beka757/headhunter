from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView
from .forms import MyUserRegisterForm
from django.contrib.auth import get_user_model
from app.models import Summary

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
    paginate_orphans = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['summaries'] = self.get_summary_objects()
        
        return context
    
    def get_object(self):
        return self.request.user
    
    def get_summary_objects(self):
        return Summary.objects.filter(user=self.request.user)

