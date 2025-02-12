from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students=[
        {'id':1, 'name': 'John', 'age':24}
    ]
    return HttpResponse(students)
# Create your views here.