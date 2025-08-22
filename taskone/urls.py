from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSet, DepartmentViewSet, AttendanceViewSet, PerformanceViewSet

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

