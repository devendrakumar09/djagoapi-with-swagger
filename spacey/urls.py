
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home),
    
    # CUSTOMER
    path('customer/',CustomerView.as_view()),
    path('customer/<id>/',CustomerViewParam.as_view()),

    # EMPLOYEE
    path('employee/',EmployeeView.as_view()),
    path('employee/<id>/',EmployeeViewParam.as_view()),


    # PRODUCT
    path('products/',ProductView.as_view()),
    path('products/<id>/',ProductViewParam.as_view()),
]
