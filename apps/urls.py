
from django.contrib import admin
from django.urls import path

from apps.views import EmployeeFormView, EmployeeListView

urlpatterns = [
    path("employee-form" ,EmployeeFormView.as_view() , name= "employee-form"),
    path("employee-list" ,EmployeeListView.as_view() , name= "employee-list")
]
