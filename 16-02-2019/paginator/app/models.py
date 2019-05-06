from django.db import models

class Student(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    contact=models.IntegerField()
    email=models.EmailField()

