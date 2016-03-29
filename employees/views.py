from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer, EmployeeListSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET',])
def employees(request):
	if request.method == 'GET':
		employees = Employee.objects.all()
		serializer = EmployeeListSerializer(employees, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def employeeById(request,id):
	if request.method == 'GET':
		if isInt(id):
			try:
				employee = Employee.objects.get(pk=id)
			except Employee.DoesNotExist :
				return Response(status=status.HTTP_204_NO_CONTENT)
			serializer = EmployeeSerializer(employee, many=False)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_204_NO_CONTENT)

def isInt(value):
  try:
    int(value)
    return True
  except:
    return False