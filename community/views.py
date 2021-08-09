import requests
from django.shortcuts import redirect, render,get_object_or_404
from django.utils import timezone
from .models import Community
from .models import Expert
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.db.models import Q
from django.contrib import messages


# def detail(request):
#     return render(request, "community/detail.html")
def communityList(request):
    communities = Community.objects.all().order_by('-pub_date')
    tag = request.GET.get('tag')
    # paginator코드
    paginator = Paginator(communities,10)
    page = request.GET.get('page')
    try:
        communities=paginator.page(page)
    except PageNotAnInteger:
        communities = paginator.page(1)
    except EmptyPage:
        communities = paginator.page(paginator.num_pages)
    if tag == 'true':
        agetag = request.GET.get('ageTag')
        communities = Community.objects.filter(age_tag=agetag).order_by('-pub_date')
        # paginator코드
        paginator = Paginator(communities,10)
        page = request.GET.get('page')
        try:
            communities=paginator.page(page)
        except PageNotAnInteger:
            communities = paginator.page(1)
        except EmptyPage:
            communities = paginator.page(paginator.num_pages)
        return render(request,'community/communityList.html', {'communities':communities})

    # 검색기능
    search_key = request.GET.get('search_key')
    if search_key:
        communities = Community.objects.filter(title__icontains=search_key)

    return render(request, "community/communityList.html", {'communities':communities})

def detail(request,id):
    community = get_object_or_404(Community, pk = id)
    writerpw = request.GET.get('writerpw')
    return render(request, "community/detail.html", {'community':community})

def expertList(request):
    experts = Expert.objects.all().order_by('-pub_date')
    tag = request.GET.get('tag')
    # paginator코드
    paginator = Paginator(experts,10)
    page = request.GET.get('page')
    try:
        experts=paginator.page(page)
    except PageNotAnInteger:
        experts = paginator.page(1)
    except EmptyPage:
        experts = paginator.page(paginator.num_pages)
    if tag == 'true':
        agetag = request.GET.get('ageTag')
        experts = Expert.objects.filter(age_tag = agetag).order_by('-pub_date')
        # paginator코드
        paginator = Paginator(experts,10)
        page = request.GET.get('page')
        try:
            experts=paginator.page(page)
        except PageNotAnInteger:
            experts = paginator.page(1)
        except EmptyPage:
            experts = paginator.page(paginator.num_pages)
        return render(request,'community/expertList.html', {'experts':experts})
    
    # 검색기능
    search_key = request.GET.get('search_key')
    if search_key:
        experts = Expert.objects.filter(title__icontains=search_key)

    return render(request, "community/expertList.html", {'experts':experts})
def expert_detail(request,ex_id):
    expert = get_object_or_404(Expert, pk = ex_id)
    return render(request, "community/expert_detail.html", {'expert':expert})

def communityWrite(request):
    return render(request, 'community/communityWrite.html')

def create(request):
    new_community = Community()
    new_community.title = request.POST['title']
    new_community.publicSetting = True
    new_community.password_Post = request.POST['pwd']
    new_community.age_tag = request.POST['opage']
    new_community.image = request.FILES.get('image')
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
    update_community.image = request.FILES.get('image')
    update_community.body = request.POST.get('body', '')
    update_community.pub_date = timezone.now()
    update_community.save()
    return redirect('community:detail', update_community.id)

def consulting(request):
    return render(request, "community/consulting.html")

def expertcreate(request):
    new_expert = Expert()
    new_expert.title = request.POST['title']
    new_expert.publicSetting = True
    new_expert.password_Post = request.POST['pwd']
    new_expert.age_tag = request.POST['opage']
    new_expert.image = request.FILES.get('image')
    new_expert.body = request.POST.get('body', '')
    new_expert.pub_date = timezone.now()
    new_expert.save()
    return redirect('community:expert_detail', new_expert.id)

def expert_edit(request,id):
    edit_expert = Expert.objects.get(id=id)
    return render(request, 'community/expert_edit.html', {'expert_edit' : edit_expert})

    
def expert_update(request, id):
    update_Expert = Expert.objects.get(id=id)
    update_Expert.title = request.POST['title']
    update_Expert.publicSetting = True
    update_Expert.password_Post = request.POST['pwd']
    update_Expert.age_tag = request.POST['opage']
    update_Expert.image = request.FILES.get('image')
    update_Expert.body = request.POST.get('body', '')
    update_Expert.pub_date = timezone.now()
    update_Expert.save()
    return redirect('community:expert_detail', update_Expert.id)

def community_delete(request, id):
    delete_community = Community.objects.get(id=id)
    delete_community.delete()
    return redirect('community:communityList')

def expert_delete(request, id):
    delete_expert = Expert.objects.get(id=id)
    delete_expert.delete()
    return redirect('community:expertList')