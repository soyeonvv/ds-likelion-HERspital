import requests
from django.shortcuts import render

def signup(request):
    return render(request, "account/signup.html")
def login(request):
    return render(request, "account/login.html")
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