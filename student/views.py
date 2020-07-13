from django.shortcuts import render


def student_main(request):
    return render(request,'student_main.html')