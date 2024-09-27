from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()  # Create a router instance
router.register(r'companies', CompanyViewSet)  # Register your viewset with the router
router.register(r'employees', EmployeeViewSet)
urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs in your project
]
