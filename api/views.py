from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializer import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(Company = company)
            emp_serializer = EmployeeSerializer(emp, many=True, context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            return Response({'message': 'currently no any employee associated with this company'})

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer