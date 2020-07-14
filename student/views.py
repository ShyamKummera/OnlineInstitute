from django.contrib import messages
from django.shortcuts import render, redirect

from student.models import StudentRegisterModel


def student_main(request):
    return render(request,'student_main.html')


def studentRegister(request):
    return render(request,'studentRegister.html')


def saveStuReg(request):
    na = request.POST.get('s1')
    cno = request.POST.get('s2')
    mail = request.POST.get('s3')
    pwd = request.POST.get('s4')
    StudentRegisterModel(name=na,contact_no=cno,Email=mail,password=pwd).save()
    messages.success(request,"Registration success")
    return redirect('studentRegister')


def studentLogin(request):
    return render(request,'studentLogin.html')


def clickLoginButton(request):
    un = request.POST.get('l1')
    pw = request.POST.get('l2')
    try:
        srm = StudentRegisterModel.objects.get(name=un,password=pw)
        return render(request,'StudentHomePage.html',{"name":un})
    except StudentRegisterModel.DoesNotExist:
        messages.error(request,"Wrong Input.Please check Your Details again")
        return redirect('studentLogin')