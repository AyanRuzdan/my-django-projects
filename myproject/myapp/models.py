from django.db import models

# Create your models here.
class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('Finance', 'Finance'),
        ('Engineering', 'Engineering'),
        ('Marketing', 'Marketing'),
    ]
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=20,choices=DEPARTMENT_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    def _str_(self):
        return self.name