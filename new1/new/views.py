from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import user_form,admin_user
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm ,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.
def signin(request):
    if request.method == 'POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=UserCreationForm()
    return render(request,'signin.html',{'form':fm})

def login_user(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request,request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                print('login sucssess ')
                return HttpResponseRedirect('/profile/')
            
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm,'name':request.user})

def profile(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            if request.user.is_superuser==True:
                fm=admin_user(request.POST,instance=request.user)
                name='admin'
                user=User.objects.all()
                
            else:
                fm=user_form(request.POST,instance=request.user)
                name='user'
            if fm.is_valid():
                fm.save()
                messages.error(request,f'sucsess fully save{request.user}')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   user data updated ')
                user=None
                
        else:
            if request.user.is_superuser==True:
                fm=admin_user(instance=request.user)
                user=User.objects.all()
            else:
                fm=user_form(instance=request.user)
                user=None
        return render(request,'profile.html',{'form':fm,'user':user,'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def change_password(request):
    if request.method == 'POST':
        fm=SetPasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            
            fm.save()
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/profile/')
    else:
        
        fm=SetPasswordForm(user=request.user)
        print(request.user)
    return render(request,'changepass.html',{'form':fm})

def user_profile(request,id):
    if request.user.is_superuser:
        pi=User.objects.get(pk=id)
        fm=admin_user(instance=pi)
        if request.method=='POST':
            fm=admin_user(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.error(request,'sucsessfully save ')
        
        else:    
            fm=admin_user(instance=pi)
        return render(request,'user_profile.html',{'pi':pi,'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    