from django.shortcuts import render
from .models import Student
# Create your views here.
def ShowIndex(request):
    return render(request,"Registration.html")


def Register(request):
    type=request.GET.get("type")

    return render(request,"Registration.html",{"type":type})


def RegisterDetails(request):
    Name=request.POST.get("t1")
    Contact=request.POST.get("t2")
    Username=request.POST.get("t3")
    Password=request.POST.get("t4")
    Student(Name=Name,Contact=Contact,Username=Username,Password=Password).save()

    return render(request,"Registration.html",{"message":"Successfully Registred"})


def LoginDetails(request):
    username=request.POST.get("u1")
    password=request.POST.get("u2")
    res=Student.objects.filter(Username=username,Password=password)
    if not res:
        return render(request,"Registration.html",{"message":"Invalid Creditials"})
    else:
        type="login"
        contact=""
        for x in res:
            contact=x.Contact

        return render(request,"Registration.html",{"name":username,"type":type,"contact":contact})


def loginForm(request):
    type=request.GET.get("type")

    return render(request,"Registration.html",{"type":type})


def ShowDetails(request):
    type=request.GET.get("type")
    contact=request.GET.get("contact")
    res=Student.objects.filter(Contact=contact)
    name=""
    contact=""
    username=""
    password=""
    for x in res:
        name=x.Name
        contact=x.Contact
        username=x.Username
        password=x.Password
    return render(request,"Registration.html",{"name":name,"contact":contact,"username":username,"password":password,"type":type})


def DeleteDetails(request):
    contact=request.POST.get("contact")
    Student.objects.filter(Contact=contact).delete()
    return render(request,"Registration.html")


def UpdateDetails(request):
    contact = request.POST.get("contact")
    res=Student.objects.filter(Contact=contact)
    type = "updatedetails"
    name = ""
    contact = ""
    username = ""
    password = ""
    for x in res:
        name = x.Name
        contact = x.Contact
        username = x.Username
        password = x.Password
    return render(request, "Registration.html",
                  {"name": name, "contact": contact, "username": username, "password": password, "type": type})


def updatedetails(request):
    Name = request.POST.get("t1")
    Contact = request.POST.get("t2")
    Username = request.POST.get("t3")
    Password = request.POST.get("t4")
    Student.objects.filter(Contact=Contact).update(Name=Name,Username=Username,Password=Password)
    return render(request, "Registration.html", {"message": "Successfully Registred"})
