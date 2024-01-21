from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog
class user_signin(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),         
        }
        
class user_login(AuthenticationForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields='__all__'
        
class add_blog(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'desc':forms.Textarea(attrs={'class':'form-control', 'rows':'3'})
                 }