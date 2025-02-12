from rest_framework import serializers
from students.models import Student 
from employees.models import Employee

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='_all_'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='_all_'