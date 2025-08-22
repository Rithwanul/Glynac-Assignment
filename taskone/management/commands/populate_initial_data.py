from django.core.management.base import BaseCommand
from taskone.models import Department, Employee
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate initial synthetic employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # Create departments
        depts = ["Engineering", "HR", "Sales", "Finance"]
        for d in depts:
            Department.objects.get_or_create(
                name=d,
                manager_name=fake.name(),
                location=fake.city(),
                headcount=0,
                budget=random.randint(50000, 200000)
            )

        # Create employees
        for _ in range(5):
            dept = random.choice(Department.objects.all())
            Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                department=dept,
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                salary=random.randint(50000, 120000),
                gender=random.choice(["Male", "Female"])
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated initial data"))

