from django.core.mail import send_mail
from django.shortcuts import render
from .models import Student
from Email import settings
from emailsending import settings as se
# Create your views here.
def ShowDetails(request):
    return render(request,"INDEX.html")


def SaveDetails(request):
    id=request.POST.get("t1")
    name=request.POST.get("t2")
    email=request.POST.get("t3")
    cno=request.POST.get("t4")
    password=name[0]
    password=password+str(len(name)+(cno[1])+name[-1])
    send_mail("new accunt password","your registration is success full","hello:"+name+"your new account password is "
                                        "auto generated\n the new password"se.EMAIL_HOST_USER)
    Student(id=id,name=name,email=email,contact=cno).save()
    return render(request,"INDEX.html")