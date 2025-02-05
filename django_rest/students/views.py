from django.shortcuts import render
from django.http import HttpResponse


# def students(request):
#     return HttpResponse('<h1>Hello</h1>')

def students(request):
    students=[
        {'id':1, 'name': 'John', 'age':24}
    ]
    return HttpResponse(students)
