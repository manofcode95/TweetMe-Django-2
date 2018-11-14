from django import forms 
from django.contrib.auth import get_user_model

User=get_user_model()

class UserForm(forms.ModelForm):
    username=forms.CharField(max_length=25)
    email= forms.CharField(max_length=25)
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'email', 'password']

        