from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from app.forms import ResponseForm
from app.models import Response
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ResponseCreateView(UserPassesTestMixin, CreateView):
    model = ResponseForm
    form_class = ResponseForm

    def test_func(self):
        return self.request.user.is_company == 0

    def get_success_url(self):
        return reverse('detail_response', kwargs={'pk': self.object.pk})
    
    
class ResponseListView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'response/list.html'
    context_object_name = 'responses'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_company == 0:
            context['responses'] = self.request.user.responses_applicant.all()
        else:
            context['responses'] = self.request.user.responses_employer.all()
            
        return context
            
            
class ResponseDetailView(UserPassesTestMixin, DetailView):
    model = Response
    template_name = 'response/detail.html'
    context_object_name = 'response'

    def test_func(self):
        return self.request.user == self.get_object().applicant or self.request.user == self.get_object().employer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = self.get_object().messeges_response.all().order_by("created_at")
        
        return context

