from django.db import models

class EmployeeRegister(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    dob=models.DateField()
    doj=models.DateField()
    gender=models.CharField(max_length=10)
    contactno=models.IntegerField()
    email=models.EmailField()
    designation=models.CharField(max_length=30)
    salary=models.IntegerField()
