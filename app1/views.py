from django.contrib import messages
from django.shortcuts import render, redirect
from app1.forms import AdminLoginForm
from app1.models import AdminLogin


def mainpage(request):
    return render(request,'mainpage.html')


def admin_main(request):
    af = AdminLoginForm()
    return render(request,'adminlogin.html',{"form":af})


def after_admin_login(request):
    ad_un = request.POST.get('username')
    ad_pw = request.POST.get('password')
    try:
        AdminLogin.objects.get(username=ad_un,password=ad_pw)
        return render(request,'AfterAdminLogin.html')
    except AdminLogin.DoesNotExist:
        messages.error(request,"incorrect username or password")
        return redirect('admin_main')
