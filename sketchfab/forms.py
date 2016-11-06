from django import forms
from django.contrib.auth.models import User

__author__ = 'Pierre Rodier | pierre@buffactory.com'


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
