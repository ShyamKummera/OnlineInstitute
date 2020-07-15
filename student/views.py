from django.contrib import messages
from django.shortcuts import render, redirect

from app1.models import ScheduleNewClass
from student.models import StudentRegisterModel, StudentEnrolDetails


def student_main(request):
    return render(request,'student_main.html')


def studentRegister(request):
    return render(request,'studentRegister.html')


def saveStuReg(request):
    na = request.POST.get('s1')
    cno = request.POST.get('s2')
    mail = request.POST.get('s3')
    pwd = request.POST.get('s4')
    sr = StudentRegisterModel.objects.values("contact_no","Email")
    c = []
    e = []
    for x in sr:
        c.append(x["contact_no"])
        e.append(x["Email"])
    if cno in c or mail in e:
        messages.error(request, "Contact Number or Email already Exist please choose another")
        return redirect('studentRegister')
    else:
        StudentRegisterModel(name=na, contact_no=cno, Email=mail, password=pwd).save()
        messages.success(request, "Registration success")
        return redirect('studentRegister')



def studentLogin(request):
    return render(request,'studentLogin.html')


def clickLoginButton(request):
    un = request.POST.get('l1')
    pw = request.POST.get('l2')
    try:
        srm = StudentRegisterModel.objects.get(name=un,password=pw)
        request.session['name']=srm.name
        return render(request,'StudentHomePage.html',{"name":un})
    except StudentRegisterModel.DoesNotExist:
        messages.error(request,"Wrong Input.Please check Your Details again")
        return redirect('studentLogin')

def StuHomeAfterLogin(request):
    res = request.session.get("name",None)
    return render(request,'StudentHomePage.html',{"name":res})


def enrolCourse(request):
    result  = request.session.get('name',None)

    if result:
        sd  = StudentRegisterModel.objects.get(name=result)
        user_cno = sd.contact_no
        enr_ad = ScheduleNewClass.objects.all()
        return render(request,'enrolStudentCourse.html',{"data":enr_ad,"d_cno":user_cno})
    else:
        return render(request,'studentLogin.html')



def yesEnrol(request):
    g_con_num = request.GET.get('cnum')
    g_cou_name = request.GET.get('cona')
    print(g_cou_name)
    print(g_con_num)
    result = request.session.get('name', None)
    if result:
        sd  = StudentRegisterModel.objects.get(name=result)
        StudentEnrolDetails(student_contact_no=g_con_num,course_name=g_cou_name).save()
        enr_ad = ScheduleNewClass.objects.all()
        messages.success(request,'You are successfully Enrolled to :')
        return render(request,'enrolStudentCourse.html',{"data":enr_ad,"course":g_cou_name})
    else:
        return render(request, 'enrolStudentCourse.html')


def viewAllEnrolCourse(request):
    result = request.session.get('name', None)
    if result:
        sd  = StudentRegisterModel.objects.get(name=result)
        c = StudentEnrolDetails.objects.all()
        return render(request,'viewAllEnrolCourse.html',{"data":c})
    else:
        return render(request, 'viewAllEnrolCourse.html')


def logoutStudent(request):
    del request.session['name']
    return redirect('mainpage')