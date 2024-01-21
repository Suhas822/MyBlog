from django import forms
from .models import students
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserR(forms.ModelForm):
    class Meta:
        model=students
        fields=['name','password']


class Teacher(UserR):
    class Meta(UserR.Meta):
        
        
        fields=['tname','password']
        
    
class auth_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username']
        
    