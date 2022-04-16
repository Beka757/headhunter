from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse
from app.forms import SummaryForm
from app.models import Summary, CATEGORY_VACANCY
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateSummaryView(CreateView):
    model = Summary
    form_class = SummaryForm
    template_name = 'summary/create_summary.html'
    extra_context = {'categories': CATEGORY_VACANCY}

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        form.instance.phone_number = self.request.user.phone
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_summary', kwargs={'pk': self.object.pk})


class DetailSummaryView(LoginRequiredMixin, DetailView):
    model = Summary
    template_name = 'summary/detail_summary.html'
    context_object_name = 'summary'


class ListSummaryView(ListView):
    template_name = 'summary/list_summary.html'
    model = Summary
    context_object_name = 'summaries'
    ordering = ['-updated_at']
    paginate_by = 20
    paginate_orphans = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summaries'] = self.get_objects().filter(publication=1)
        
        return context
    
    def get_objects(self):
        return self.model.objects.all()
