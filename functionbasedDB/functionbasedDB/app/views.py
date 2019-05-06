from django.shortcuts import render
from.models import EmployeeRegister

# Create your views here.
def ShowIndex(request):
    qs=EmployeeRegister.objects.all()
    return render(request,"EMployeeRegister.html",{"res":qs})


def Employeeregister(request):
    idno=request.POST.get("p1")
    name=request.POST.get("p2")
    dob=request.POST.get("p3")
    doj=request.POST.get("p4")
    gender=request.POST.get("p5")
    cno=request.POST.get("p6")
    email=request.POST.get("p7")
    des=request.POST.get("p8")
    salary=request.POST.get("p9")
    EmployeeRegister(id=idno,name=name,dob=dob,doj=doj,gender=gender,contactno=cno,email=email,designation=des,salary=salary).save()
    qs = EmployeeRegister.objects.all()
    return render(request,"EMployeeRegister.html",{"message":"Employee Details Saved SuccessFully","res":qs})


def showDetails(request):
    type=request.GET.get("type")
    email=request.GET.get("email")
    res=EmployeeRegister.objects.filter(email=email)
    id=""
    name=""
    dob=""
    gender=""
    doj=""
    contact=""
    email=""
    des=""
    salary=""
    for x in res:
        id=x.id
        name=x.name
        dob=x.dob
        gender=x.gender
        doj=x.doj
        contact=x.contactno
        email=x.email
        des=x.designation
        salary=x.salary
    qs = EmployeeRegister.objects.all()

    return render(request,"EMployeeRegister.html",{"data":res,"type":type,"id":id,"name":name,
                                                   "dob":dob,"doj":doj,"gender":gender,"contact":contact,
                                                   "email":email,"des":des,"salary":salary,"res":qs})


def UpdateDetails(request):
    type=request.GET.get("type")
    email=request.GET.get("email")
    res1=EmployeeRegister.objects.filter(email=email)
    qs = EmployeeRegister.objects.all()
    return render(request,"EMployeeRegister.html",{"type":type,"res1":res1,"res":qs})


def UpdateEmployeeDetails(request):
    id=request.POST.get("p1")
    name=request.POST.get("p2")
    # dob=request.POST.get("p3")
    # doj=request.POST.get("p4")
    gender=request.POST.get("p5")
    contact=request.POST.get("p6")
    email=request.POST.get("p7")
    des=request.POST.get("p8")
    salary=request.POST.get("p9")
    EmployeeRegister.objects.filter(email=email).update(name=name,contactno=contact)
    qs = EmployeeRegister.objects.all()
    return render(request,"EMployeeRegister.html",{"message":"Updated Successfullly","res":qs})


def DeleteDetails(request):
    email=request.GET.get("email")
    print(email)
    EmployeeRegister.objects.filter(email=email).delete()
    qs = EmployeeRegister.objects.all()
    return render(request,"EMployeeRegister.html",{"res":qs})