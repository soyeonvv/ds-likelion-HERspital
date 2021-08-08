import requests
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

#Authen=로그인, UserCre=회원가입

def signup(request):
    return render(request, "account/signup.html")

def login_view(request):
  if request.method=='POST':
    form=AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username=form.cleaned_data.get("username")
      password=form.cleaned_data.get("password")
      user=authenticate(request=request, username=username, password=password)
      if user is not None:
        login(request, user)

    return redirect("mainpage")

  else: 
    form=AuthenticationForm()
    return render(request, "account/login.html",{'form':form})

def logout_view(request):
  logout(request)
  return redirect("mainpage")

def register_view(request):
  if request.method=="POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user=form.save()
      login(request, user)
    return redirect('mainpage')

  else:
    form = UserCreationForm()
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