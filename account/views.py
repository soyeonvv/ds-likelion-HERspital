import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

from django.contrib.auth.models import User
from django.contrib import auth
from .models import CustomUser
# from .models import Setting
from django.contrib.auth.hashers import check_password
from .forms import CheckPasswordForm
from django.contrib import messages
from account.decorators import login_message_required


#Authen=로그인, UserCre=회원가입

# def signup(request):
#     return render(request, "account/signup.html")


def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = CustomUser.objects.get(username = request.POST['username'])
    
    # user = auth.authenticate(request, username=username, password=password)
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

#       user=authenticate(request=request, username=username, password=password)
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
  if request.method == 'POST':
    
    if request.POST['password'] == request.POST['password2']:
      try:
        user = CustomUser.objects.get(username = request.POST['username'])
        return render(request, 'account/signup.html', {'error':'Username has already been taken.'})
      except CustomUser.DoesNotExist:
        user = CustomUser.objects.create_user(
          request.POST['username'], #create_user가 username만 파라미터 받아서 다른 것은 직접 연결해줌
          password = request.POST['password'], 
          nickname = request.POST['nickname'],
          birth = request.POST['birth'],
          gender = request.POST['gender'],
          email = request.POST['email'],
          position = request.POST['position'], 
          workplace = request.POST['workplace'],
          certifyImg = request.POST['certifyImg']
          )
        auth.login(request,user)
        return redirect("mainpage")
    else:
      return render(request, 'account/signup.html')
  return render(request, 'account/signup.html')


# def signup(request):
#   if request.method=="POST":
#     form = RegisterForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#     return redirect('mainpage')
#   else:
#     form = RegisterForm()
#     return render(request, 'account/signup.html',{'form':form})
    
def mypage(request):
    return render(request, "account/mypage.html")

def setting(request):
    return render(request, "account/setting.html")

# def update2(request ,id):
#     update_setting = Setting.objects.get(id=id)
#     update_setting.postcode = request.POST['postcode']
#     update_setting.address = request.POST['address']
#     update_setting.extraAddress = request.POST['extraAddress']
#     update_setting.save()
#     return redirect('account:mypage', update_setting.id)

@login_message_required
def userDelete(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/core/mainpage/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'account/userDelete.html', {'password_form':password_form})
