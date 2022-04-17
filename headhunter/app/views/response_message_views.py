from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from app.forms import ResponseForm
from app.models import Response


class ResponseCreateView(CreateView):
    model = ResponseForm
    form_class = ResponseForm
    
    def get_success_url(self):
        return reverse('detail_response', kwargs={'pk': self.object.pk})
    
    
class ResponseListView(ListView):
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
            
            
class ResponseDetailView(DetailView):
    model = Response
    template_name = 'response/detail.html'
    context_object_name = 'response'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = self.get_object().messeges_response.all().order_by("created_at")
        
        return context

