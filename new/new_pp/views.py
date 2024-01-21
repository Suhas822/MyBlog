from django.shortcuts import render,HttpResponseRedirect
from .forms import UserR,Teacher
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import auth_form

def sign_up(request):
    if request.method=='POST':
        fm=auth_form(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm=auth_form()
    return render(request,'signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            
            if fm.is_valid():
                unama=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=unama,password=upass)
                if user is not None:
                    login(request,user)
                    print("login sucsessfull")
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
        
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        print("user not authenticate ")
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')