import requests
from django.shortcuts import redirect, render,get_object_or_404
from django.utils import timezone
from .models import Community
from .models import Expert

# def detail(request):
#     return render(request, "community/detail.html")
def communityList(request):
    communities = Community.objects.all().order_by('-pub_date')
    tag = request.GET.get('tag')
    if tag == 'true':
        agetag = request.GET.get('ageTag')
        communities = Community.objects.filter(age_tag=agetag).order_by('-pub_date')
        return render(request,'community/communityList.html', {'communities':communities})
    return render(request, "community/communityList.html", {'communities':communities})

def detail(request,id):
    community = get_object_or_404(Community, pk = id)
    return render(request, "community/detail.html", {'community':community})

def expertList(request):
    experts = Expert.objects.all()
    tag = request.GET.get('tag')
    if tag == 'true':
        agetag = request.GET.get('ageTag')
        experts = Expert.objects.filter(age_tag = agetag).order_by('-pub_date')
        return render(request,'community/expertList.html', {'experts':experts})
    return render(request, "community/expertList.html", {'experts':experts})
def expert_detail(request,ex_id):
    expert = get_object_or_404(Expert, pk = ex_id)
    return render(request, "community/expert_detail.html", {'expert':expert})
def consulting(request):
    return render(request, "community/consulting.html")

def communityWrite(request):
    return render(request, 'community/communityWrite.html')

def create(request):
    new_community = Community()
    new_community.title = request.POST['title']
    new_community.publicSetting = True
    new_community.password_Post = request.POST['pwd']
    new_community.age_tag = request.POST['opage']
    new_community.image = request.FILES['image']
    new_community.body = request.POST.get('body', '')
    new_community.pub_date = timezone.now()
    new_community.save()
    return redirect('community:detail', new_community.id)

def communityedit(request,id):
    edit_community = Community.objects.get(id=id)
    return render(request, 'community/communityedit.html', {'edit' : edit_community})
    
def update(request, id):
    update_community = Community.objects.get(id=id)
    update_community.title = request.POST['title']
    update_community.publicSetting = True
    update_community.password_Post = request.POST['pwd']
    update_community.age_tag = request.POST['opage']
    update_community.image = request.FILES['image']
    update_community.body = request.POST.get('body', '')
    update_community.pub_date = timezone.now()
    update_community.save()
    return redirect('community:detail', update_community.id)

