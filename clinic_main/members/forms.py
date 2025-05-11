from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser,Patient,Staff

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('family_user', 'name_user', 'middle_name', 'email', 'phone')


class PatientSignUpForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['polis_num']

class StaffSignUpForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['position']