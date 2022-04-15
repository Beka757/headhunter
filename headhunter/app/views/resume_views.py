from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse
from app.forms import SummaryForm
from app.models import Summary, CATEGORY_VACANCY


class TestHomeView(TemplateView):
    template_name = 'home.html'


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


class DetailSummaryView(DetailView):
    model = Summary
    template_name = 'summary/detail_summary.html'
    context_object_name = 'summary'
