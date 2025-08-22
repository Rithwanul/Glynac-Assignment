from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, Department, Attendance, Performance
from .serializers import EmployeeSerializer, DepartmentSerializer, AttendanceSerializer, PerformanceSerializer
from .throttles import StandardUserThrottle, StandardAnonThrottle
import logging

# Setup logger
logger = logging.getLogger("api_logger")

# Helper function for consistent API responses
def api_response(success, message="", data=None, errors=None, status_code=status.HTTP_200_OK):
    response = {
        "success": success,
        "message": message,
        "data": data,
        "errors": errors
    }
    logger.info(response)  # log every response
    return Response(response, status=status_code)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    throttle_classes = [StandardUserThrottle, StandardAnonThrottle]

    def list(self, request, *args, **kwargs):
        logger.info(f"GET /departments/ by {request.user}")
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return api_response(True, "Departments retrieved successfully", serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving departments: {str(e)}")
            return api_response(False, "Failed to retrieve departments", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [StandardUserThrottle, StandardAnonThrottle]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee', 'date']
    throttle_classes = [StandardUserThrottle, StandardAnonThrottle]

    def get_queryset(self):
        queryset = super().get_queryset()
        employee_id = self.request.query_params.get('employee')
        month = self.request.query_params.get('month')  # e.g., '2025-08'

        if employee_id:
            queryset = queryset.filter(employee__id=employee_id)
        if month:
            year, mon = month.split('-')
            queryset = queryset.filter(date__year=year, date__month=mon)
        logger.info(f"GET /attendance/ by {self.request.user} - filtered by employee={employee_id}, month={month}")
        return queryset

    def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return api_response(True, "Attendance retrieved successfully", serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving attendance: {str(e)}")
            return api_response(False, "Failed to retrieve attendance", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    throttle_classes = [StandardUserThrottle, StandardAnonThrottle]

    def list(self, request, *args, **kwargs):
        logger.info(f"GET /performance/ by {request.user}")
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return api_response(True, "Performance retrieved successfully", serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving performance: {str(e)}")
            return api_response(False, "Failed to retrieve performance", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

