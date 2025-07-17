from django.db import models
from django.contrib.auth.models import User

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

COURSE_TYPE = (
    ("english", "English"),
    ("programming", "Programming"),
    ("design", "Design"),
    ("machine_learning", "Machine Learning"),
    ("osint", "OSINT")
)

STATUS = (
    (0, "Unvailable"),
    (1, "Available")
)

class Course(models.Model):
    course_name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    course_type = models.CharField(max_length=200, choices=COURSE_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name