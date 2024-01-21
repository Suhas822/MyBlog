from django.shortcuts import render,HttpResponseRedirect
from .forms import user_signin,user_login,add_blog
from .models import Blog
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import Group
# Create your views here
def home(request):
    fm=Blog.objects.all()
    return render(request,'blog/home.html',{'form':fm})

def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=user_signin(request.POST)
            if fm.is_valid():
                user=fm.save()
                group=Group.objects.get(name='Writer')
                user.groups.add(group)
                messages.success(request,"Register  in successfully")
                return HttpResponseRedirect('/login/')
                
        else:
            fm=user_signin()
        return render(request,'blog/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/Dashboard/')
def user_log(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=user_login(request,request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    print(request)
                    print('66666666666666666666666666666666666666666')
                    print(user)
                    messages.success(request,f"login in successfully{user}")
                    return HttpResponseRedirect('/Dashboard/')
                    
        else:        
            fm=user_login()
        return render(request,'blog/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/Dashboard/')

def About(request):
    return render(request,'blog/about.html')
    

def user_logout(request):
    logout(request)
    messages.success(request,"logout in successfully")
    return HttpResponseRedirect('/home/')
    
def helps(request):
    return render(request,'blog/helps.html')

def user_Dashboard(request):
    user=(request.user)
    user_fullname=user.get_full_name()
    fm=Blog.objects.all()
    return render(request,'blog/Dashboard.html',{'form':fm,'user_fullname':user_fullname})
    

def add_blogs(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=add_blog(request.POST)
            if fm.is_valid():
                
                fm.save()
                messages.success(request,"new Blog add successfully")
                return HttpResponseRedirect('/Dashboard/')
        else:
            fm=add_blog()
        return render(request,'blog/Addblog.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
        
def update_blog(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Blog.objects.get(pk=id)
            fm=add_blog(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Blog Update successfully')
                return HttpResponseRedirect('/Dashboard/')
        else:
            pi=Blog.objects.get(pk=id)
            fm=add_blog(instance=pi)
        return render(request,'blog/updateblog.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
def delete_blog(request,id):
    if request.method=='POST':
        pi=Blog.objects.get(pk=id)
        pi.delete()
        messages.success(request,'Blog Deleted successfully')
        return HttpResponseRedirect('/Dashboard/')
    else:
        return HttpResponseRedirect('/login/')
        