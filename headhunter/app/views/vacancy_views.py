from django.views.generic import CreateView, DetailView, ListView, TemplateView
from app.models import Vacancy, CATEGORY_VACANCY
from app.forms import VacancyForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator


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


class DetailVacancyView(LoginRequiredMixin, DetailView):
    model = Vacancy
    template_name = 'vacancy/detail_vacancy.html'
    context_object_name = 'vacancy'

    def test_func(self):
        return self.request.user == self.get_object().user


class ListVacancyView(ListView):
    template_name = 'vacancy/list_vacancy.html'
    model = Vacancy
    paginate_related_by = 20
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        vacancies = Vacancy.objects.filter(publication='True').order_by('-updated_at')
        paginator = Paginator(
            vacancies, self.paginate_related_by,
            self.paginate_related_orphans
        )
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['title'] = 'Список вакансии'
        kwargs['vacancies'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        kwargs['categories'] = CATEGORY_VACANCY
        return super().get_context_data(**kwargs)


class VacancyCategoryView(TemplateView):
    template_name = 'vacancy/list_vacancy.html'

    def filter_vacansy_by_category(self, category):
        return Vacancy.objects.filter(category__iexact=category, publication='True').order_by('-updated_at')

    def get_context_data(self, **kwargs):
        category = self.kwargs.get('category')
        kwargs['vacancies'] = self.filter_vacansy_by_category(category)
        kwargs['title'] = category.capitalize
        kwargs['categories'] = CATEGORY_VACANCY
        return super().get_context_data(**kwargs)


class SearchView(View):
    def get(self, request, *args, **kwargs):
        search_param = request.GET.get('query')
        categories = CATEGORY_VACANCY
        result = Vacancy.objects.filter(
            Q(vacancy_position__icontains=search_param, publication='True')
        )
        return render(request, 'vacancy/list_vacancy.html', {'vacancies': result, 'categories': categories})
