from django.urls import path
from .import views

urlpatterns =[
    path('',views.students),
    path('students/',views.students),
]