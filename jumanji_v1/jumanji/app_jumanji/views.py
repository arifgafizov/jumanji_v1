from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancies.html')


#class VacanciesSpecialtiesView(View):
#    def get(self, request, cat, frontend):
#        context = {
#            'cat': cat,
#            'frontend': frontend
#        }
#        return render(request, 'vacancies.html', context=context)

class CompaniesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'companies.html')
