from django.urls import path
from . import views

urlpatterns =[
    path('students/', views.studentsView),
    # here url will handle the get, put request all at one
    path('students/<int:pk>', views.studentDetailView),
    # path('employees/', views.Employee.as_view()),
]