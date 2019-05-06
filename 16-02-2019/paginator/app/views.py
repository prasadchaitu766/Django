from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator

# Create your views here.
def ShowIndex(request):
    no=request.GET.get("pageno")
    qs=Student.objects.all()
    p=Paginator(qs,2)
    if no==None:
        p=p.page(1)
    else:
        p=p.page(no)
    return render(request,"index.html",{"res":p})
def SaveDetails(request):
    id=request.POST.get("t1")
    name=request.POST.get("t2")
    contact=request.POST.get("t3")
    email=request.POST.get("t4")
    Student(Id=id,Name=name,contact=contact,email=email).save()
    return ShowIndex(request)