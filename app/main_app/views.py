from django.shortcuts import render
from main_app.models import NotEmployed, Employed
from django.http import HttpResponse

# Create your views here.
def index(request):
    _context = {
        'nbar': 'home'
    }
    return render(request, 'main_app/index.html', context=_context)

def about(request):

    non_employees = NotEmployed.objects.all()
    employees = Employed.objects.all()

    _context = {
        'nbar': 'about',
        'non_employees': non_employees,
        'employees': employees,
    }

    print(request.POST)

    return render(request, 'main_app/about.html', context=_context)