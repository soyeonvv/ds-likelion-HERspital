import requests
from django.shortcuts import render

def signup(request):
    return render(request, "account/signup.html")
def login(request):
    return render(request, "account/login.html")