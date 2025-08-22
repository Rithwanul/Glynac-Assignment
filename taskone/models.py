from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    manager_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    headcount = models.IntegerField()
    budget = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    salary = models.FloatField()
    gender = models.CharField(max_length=10)

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # Present/Absent
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    work_hours = models.FloatField()

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=10)
    tasks_completed = models.IntegerField()
    rating = models.IntegerField()
    bonus = models.FloatField()
    remarks = models.TextField()
    late_days = models.IntegerField()

