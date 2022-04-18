from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView
from django.urls import reverse
from app.forms import SummaryForm, WorkExperienceForm, EducationForm
from app.models import Summary, CATEGORY_VACANCY, Education, WorkExperience
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator
from django.views import View
from django.shortcuts import redirect, render
from django.db.models import Q


class CreateSummaryView(UserPassesTestMixin, CreateView):
    model = Summary
    form_class = SummaryForm
    template_name = 'summary/create_summary.html'
    extra_context = {'categories': CATEGORY_VACANCY}

    def test_func(self):
        return self.request.user.is_company == 0

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        form.instance.phone_number = self.request.user.phone
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_summary', kwargs={'pk': self.object.pk})


class DetailSummaryView(UserPassesTestMixin, DetailView):
    model = Summary
    template_name = 'summary/detail_summary.html'
    context_object_name = 'summary'

    def test_func(self):
        return self.request.user == self.get_object().user or self.request.user.is_company == 1


class ListSummaryView(UserPassesTestMixin, ListView):
    template_name = 'summary/list_summary.html'
    model = Summary
    context_object_name = 'summaries'
    ordering = ['-updated_at']
    paginate_related_by = 20
    paginate_related_orphans = 0

    def test_func(self):
        return self.request.user.is_company == 1

    def get_context_data(self, **kwargs):
        summaries = Summary.objects.filter(publication='True').order_by('-updated_at')
        paginator = Paginator(
            summaries, self.paginate_related_by,
            self.paginate_related_orphans
        )
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['title'] = 'Список резюме'
        kwargs['summaries'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        kwargs['categories'] = CATEGORY_VACANCY
        
        return super().get_context_data(**kwargs)
    
    def get_objects(self):
        return self.model.objects.all()


class SummaryCategoryView(TemplateView):
    template_name = 'summary/list_summary.html'

    def filter_summary_by_category(self, category):
        return Summary.objects.filter(category__iexact=category, publication='True').order_by('-updated_at')

    def get_context_data(self, **kwargs):
        category = self.kwargs.get('category')
        kwargs['summaries'] = self.filter_summary_by_category(category)
        kwargs['title'] = category.capitalize
        kwargs['categories'] = CATEGORY_VACANCY
        return super().get_context_data(**kwargs)


class SummarySearchView(View):
    def get(self, request, *args, **kwargs):
        search_param = request.GET.get('query')
        categories = CATEGORY_VACANCY
        result = Summary.objects.filter(
            Q(summary_position__icontains=search_param, publication='True')
        ).order_by('-updated_at')
        return render(request, 'summary/list_summary.html', {
            'summaries': result,
            'categories': categories
        })
        

class UpdateSummaryView(UserPassesTestMixin, UpdateView):
    template_name = 'summary/update_summary.html'
    form_class = SummaryForm
    model = Summary
    context_object_name = 'summary'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = CATEGORY_VACANCY
        context['work_experiences'] = self.get_object().work_experience.all()
        context['educations'] = self.get_object().education.all()
        
        return context

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        return reverse('detail_summary', kwargs={'pk': self.object.pk})
    
    
class UpdateWorkExperienceView(UpdateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    
    def get_success_url(self):
        return reverse('update_summary', kwargs={'pk': self.kwargs['summary_pk']})


class UpdateEducationView(UpdateView):
    model = Education
    form_class = EducationForm
    
    def get_success_url(self):
        return reverse('update_summary', kwargs={'pk': self.kwargs['summary_pk']})

