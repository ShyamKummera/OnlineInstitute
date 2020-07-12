from django import forms
from django.contrib.admin import widgets
from django.forms import SelectDateWidget

from app1.models import ScheduleNewClass


class AdminLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=5,widget=forms.PasswordInput)


class ScheduleClassForm(forms.ModelForm):
    date_course_start =forms.DateField(widget=SelectDateWidget)
    time_start = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder':"HH:MM am"}))

    class Meta:
        model = ScheduleNewClass
        fields = '__all__'
    def clean_fee(self):
        fee = self.cleaned_data['fee']
        if fee >= 3000:
            return fee
        else:
            raise forms.ValidationError('Fee must be Greater than 3000')



