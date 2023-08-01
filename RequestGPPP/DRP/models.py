from django.db import models

# Create your models here.


class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField(null=True)
    #PhotoFileName = models.CharField(max_length=500)
    PhotoFileName=models.ImageField(upload_to='Photos/',max_length=100)

