import requests
from django.shortcuts import render

def detail(request):
    return render(request, "community/detail.html")