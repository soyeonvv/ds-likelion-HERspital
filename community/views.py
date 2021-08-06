import requests
from django.shortcuts import render,get_object_or_404
from .models import Community

# def detail(request):
#     return render(request, "community/detail.html")
def communityList(request):
    communities = Community.objects.all()
    return render(request, "community/communityList.html", {'communities':communities})
def detail(request,id):
    community = get_object_or_404(Community, pk = id)
    return render(request, "community/detail.html", {'community':community})
def expertList(request):
    return render(request, "community/expertList.html")
def consulting(request):
    return render(request, "community/consulting.html")
def communityWrite(request):
    return render(request, "community/communityWrite.html")