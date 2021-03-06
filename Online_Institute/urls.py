"""Online_Institute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from app1 import views
from student import urls as st

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(st)),
# --------------------------------------------------
    path('',views.mainpage,name="mainpage"),
# -----------------admin main button--------------------------
    path('admin_main/',views.admin_main,name="admin_main"),
    path('after_admin_login/',views.after_admin_login,name="after_admin_login"),
    path('AdminLoginHome/',TemplateView.as_view(template_name='AfterAdminLogin.html'),name="AdminLoginHome"),
# -----------------schedule new class-----------------------------------------------
    path('sch_new_class/',views.sch_new_class,name="sch_new_class"),
    path('schNewClassDatabase/',views.schNewClassDatabase,name="schNewClassDatabase"),
# ------------------View all Schedule classes-----------------------------------------------
    path('ViewAllClasses/',views.ViewAllClasses,name="ViewAllClasses"),
    path('updateCourse/',views.updateCourse,name="updateCourse"),
    path('updatedSuccess/',views.updatedSuccess,name="updatedSuccess"),
    path('deleteCourse/',views.deleteCourse,name="deleteCourse"),

]
