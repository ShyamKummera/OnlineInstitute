from django.contrib import messages
from django.shortcuts import render, redirect
from app1.forms import AdminLoginForm, ScheduleClassForm
from app1.models import AdminLogin, ScheduleNewClass


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


def sch_new_class(request):
    snc = ScheduleClassForm()
    return render(request,'scheduleNewClass.html',{"form":snc})


def schNewClassDatabase(request):
    scfd = ScheduleClassForm(request.POST)
    if scfd.is_valid():
        scfd.save()
        messages.success(request,"Details Added Successfully")
        return redirect('sch_new_class')
    else:
        return render(request,'scheduleNewClass.html',{"form":scfd})


def ViewAllClasses(request):
    sc = ScheduleNewClass.objects.all()
    return render(request,'ViewAllClasses.html',{"data":sc})


def updateCourse(request):
    fif = request.GET.get("cid")
    up = ScheduleNewClass.objects.get(course_id=fif)
    return render(request,'updateCourse.html',{"data":up})


def updatedSuccess(request):
    id = request.POST.get('u1')
    c_name =request.POST.get('u2')
    fac = request.POST.get('u3')
    date = request.POST.get('u4')
    time = request.POST.get('u5')
    fair = request.POST.get('u6')
    days = request.POST.get('u7')

    return None