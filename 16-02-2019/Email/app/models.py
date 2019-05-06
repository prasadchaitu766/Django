from django.db import models

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    contact=models.IntegerField()
