# from django.shortcuts import render
# from django.http import JsonResponse

# def studentsView(request):
#     students={
#         'id':1,
#         'name': 'John',
#         'class':'Computer Science',
#     }
#     return JsonResponse(students)  

# manual serialization

# from django.shortcuts import render
# from django.http import JsonResponse
# from students.models import Student
# def studentsView(request):
#     students = Student.objects.all()
#     students_list= list(students.values())
#     return JsonResponse(students_list, safe=False)
# Create your views here.

from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
    # Get all the data from the student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =='POST':
        # here post request accepting the incoming the data (data=request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  

    if request.method == 'GET':
        serializer = StudentSerializer(student) 
        return Response(serializer.data, status=status.HTTP_200_OK)    