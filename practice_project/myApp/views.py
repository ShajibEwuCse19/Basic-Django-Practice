from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from myApp import forms

from .models import students


# Create your views here.
def home(request):
    students_list = students.objects.order_by('name')

    diction = {'students' : students_list}
    return render(request, 'myApp/index.html', context=diction)


def form(request):
    new_form = forms.studentForm
    diction = {'test_form' : new_form}
    return render(request, 'myApp/form.html', context=diction)
