from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Department

# Create your views here.


def index(request):
    context = {}
    context['departments'] = Department.objects.order_by('name','location')[:12]
    return render(request, 'guitars/index.html', context)

class DepartmentListView(ListView):
    model = Department

def about(request):
    context = {}
    return render(request, 'guitars/about.html', context)