from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancies.html')


class VacanciesSpecialtiesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy.html')

class CompaniesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'company.html')

class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy.html')