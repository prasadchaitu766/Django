from django.db import models

# Create your models here.
class category(models.Model):
    image=models.FileField(null=True,blank=True)
    name=models.CharField(max_length=270)
    slug=models.SlugField(unique=True)
    publicatin_status=models.BooleanField()
    def __str__(self):
        return self.name
class Manufactuar(models.Model):
    image=models.FileField(null=True,blank=True)
    name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    publication_status=models.BooleanField()
    def __str__(self):
        return self.name
class product(models.Model):
    name=models.CharField(max_length=290)
    slug=models.SlugField(null=True,blank=True)
    details=models.TextField()
    price=models.SmallIntegerField()
    quantity=models.SmallIntegerField()
    stock_level=models.SmallIntegerField()
    category_id=models.ForeignKey(category,on_delete=True)
    manufactuar_id=models.ForeignKey(Manufactuar,on_delete=True)
    publication_status=models.BooleanField()
    def __str__(self):
        return self.name
