from django.core.management.base import BaseCommand
from taskone.models import Department, Employee, Attendance, Performance
from faker import Faker
import random
from datetime import timedelta, date, time

class Command(BaseCommand):
    help = 'Populate initial synthetic employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # --- Create departments ---
        depts = ["Engineering", "HR", "Sales", "Finance"]
        for d in depts:
            Department.objects.get_or_create(
                name=d,
                manager_name=fake.name(),
                location=fake.city(),
                headcount=0,
                budget=random.randint(50000, 200000)
            )

        # --- Create employees ---
        employees = []
        for _ in range(5):
            dept = random.choice(Department.objects.all())
            emp = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                department=dept,
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                salary=random.randint(50000, 120000),
                gender=random.choice(["Male", "Female"])
            )
            employees.append(emp)

        # --- Create attendance records (last 30 days) ---
        for emp in employees:
            for n in range(30):
                att_date = date.today() - timedelta(days=n)
                status = random.choice(["Present", "Absent"])
                check_in = fake.time_object() if status == "Present" else None
                check_out = fake.time_object() if status == "Present" else None
                work_hours = round(random.uniform(6, 9), 2) if status == "Present" else 0
                Attendance.objects.create(
                    employee=emp,
                    date=att_date,
                    status=status,
                    check_in_time=check_in,
                    check_out_time=check_out,
                    work_hours=work_hours
                )

        # --- Create performance records (last 6 months) and link attendance ---
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for emp in employees:
            for m in months[-6:]:  # last 6 months
                # Get all attendance for that month
                month_num = months.index(m) + 1
                attendance_for_month = Attendance.objects.filter(
                    employee=emp,
                    date__month=month_num
                )
                tasks_completed = random.randint(5, 20)
                rating = random.randint(1, 5)
                bonus = round(random.uniform(1000, 5000), 2)
                remarks = fake.sentence()
                
                perf = Performance.objects.create(
                    employee=emp,
                    month=m,
                    tasks_completed=tasks_completed,
                    rating=rating,
                    bonus=bonus,
                    remarks=remarks
                )
                
                # Link attendance records
                perf.attendance_records.set(attendance_for_month)

        self.stdout.write(self.style.SUCCESS(
            "Successfully populated departments, employees, attendance, and performance data"
        ))

