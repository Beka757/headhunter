from django.views.generic import CreateView, DetailView
from app.models import Vacancy, CATEGORY_VACANCY
from app.forms import VacancyForm
from django.urls import reverse


class VacancyCreateView(CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'vacancy/create_vacancy.html'
    extra_context = {'categories': CATEGORY_VACANCY}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class DetailVacancyView(DetailView):
    model = Vacancy
    template_name = 'vacancy/detail_vacancy.html'
    context_object_name = 'vacancy'
