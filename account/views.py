import requests
from django.shortcuts import render

def signup(request):
    return render(request, "account/signup.html")