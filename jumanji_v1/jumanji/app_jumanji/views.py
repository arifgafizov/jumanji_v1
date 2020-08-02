from django.shortcuts import render, get_object_or_404
from django.views import View

from app_jumanji.models import Specialty, Company, Vacancy

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'specialties': Specialty.objects.all(),
            'companies': Company.objects.all()
        }
        return render(request, 'base.html', context=context)


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'vacancies': Vacancy.objects.all()
        }
        return render(request, 'vacancies.html', context=context)


class VacanciesSpecialtiesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy.html')

class CompaniesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'company.html')

class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy.html')