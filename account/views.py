import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

from django.contrib.auth.models import User
from django.contrib import auth

#Authen=로그인, UserCre=회원가입

# def signup(request):
#     return render(request, "account/signup.html")


def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('mainpage')
    else:
      return render(request, 'account/login.html', {'error':'username or password is incorrect'})
  else:
    return render(request, 'account/login.html')


# def login_view(request):
#   if request.method=='POST':
#     form=AuthenticationForm(request=request, data=request.POST)

#     if form.is_valid():
#       username = form.cleaned_data.get("username")
#       password = form.cleaned_data.get("password")

#       user=authenticate(
#         request=request,
#         username=username,
#         password=password
#         )
#       if request.user is not None:
#         login(request, user)
#     return redirect("mainpage")
#   else: 
#     form=AuthenticationForm()
#   return render(request, "account/login.html",{'form':form})

def logout_view(request):
  logout(request)
  return redirect("mainpage")

def signup(request):
  if request.method=="POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
    return redirect('mainpage')
  else:
    form = RegisterForm()
    return render(request, 'account/signup.html',{'form':form})
    
def mypage(request):
    return render(request, "account/mypage.html")
def setting(request):
    return render(request, "account/setting.html")
def stchange(request):
    return render(request, "account/stchange.html")
def stcancel(request):
    return render(request, "account/stcancel.html")
def stdelete(request):
    return render(request, "account/stdelete.html")