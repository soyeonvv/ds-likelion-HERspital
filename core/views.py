import requests
<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Review
from django.utils import timezone
# Create your views here.
def mainpage(request):
    name = request.GET.get('name')
    reviews = Review.objects.all().order_by('-pub_date')
    if name == 'true':
        hospital = request.GET.get('hospital')
        reviews = Review.objects.filter(hospital = hospital).order_by('-pub_date')
        return render(request, "core/mainpage.html", {'reviews':reviews})
    return render(request, "core/mainpage.html",{'reviews':reviews})

def create_review(request):
    new_review = Review()
    new_review.author = request.user
    new_review.body = request.POST.get('new_review')
    new_review.pub_date = timezone.now()
    new_review.hospital = request.POST.get('hospital_Name')
    new_review.rating = request.POST.get('rating')
    new_review.save()
    return redirect('core:mainpage')
=======
from django.shortcuts import render


# Create your views here.
def mainpage(request):
    return render(request, "core/mainpage.html")
>>>>>>> 6cf177a17340d55ea548a210761dc2d6723dca1c
