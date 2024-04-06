from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics




@api_view(['GET'])
def home(request):    
    return Response({
        'status':200,
        'payload': "WELCOME TO DEVENDRA KUMAR PROJECT"
    })

# CUSTOMER
class CustomerView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerViewParam(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'

# EMPLOYEE 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class EmployeeView(generics.ListAPIView,generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeViewParam(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'

# PRODUCT 
class ProductView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewParam(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'