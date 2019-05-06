from django.db import models
class Student(models.Model):
    Name=models.CharField(max_length=20)
    Contact=models.IntegerField(primary_key=True)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

