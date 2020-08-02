from django.shortcuts import render, Http404
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
    def get(self, request, code):
        specialty = Vacancy.objects.filter(specialty__code=code).first()
        if not specialty:
            raise Http404
        context = {
            'specialty': specialty,
            'vacancies': Vacancy.objects.all()
        }
        return render(request, 'vacancies.html', context=context)

class CompaniesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'company.html')

class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy.html')