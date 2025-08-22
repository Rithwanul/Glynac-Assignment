from rest_framework import viewsets
from .models import Employee, Department, Attendance, Performance
from .serializers import EmployeeSerializer, DepartmentSerializer, AttendanceSerializer, PerformanceSerializer
from django_filters.rest_framework import DjangoFilterBackend  # <-- add this

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'date'] 

    def get_queryset(self):
        queryset = super().get_queryset()
        employee_id = self.request.query_params.get('employee')
        month = self.request.query_params.get('month')  # e.g., '2025-08'

        if employee_id:
            queryset = queryset.filter(employee__id=employee_id)
        if month:
            year, mon = month.split('-')
            queryset = queryset.filter(date__year=year, date__month=mon)
        return queryset 


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

