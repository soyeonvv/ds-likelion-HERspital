from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
  nickname = models.CharField(max_length=100,default='') #이름
  email = models.EmailField(max_length=100,default='') #이메일
  birth = models.DateField(blank=True,null=True) #생년월일
  gender = models.CharField(max_length=50, default='') #성별
  position = models.CharField(max_length=50, default='normal') #일반인/전문인
  certifyImg = models.ImageField(upload_to="account/", blank=True, null=True) #자격증사진 - 전문인일때 무조건 받아야하는데 어떻게 해야하지..
  workplace = models.CharField(max_length=50, blank=True) #의료기관 - 전문인일때 무조건 받아야하는데 어떻게 해야하지..
  postcode = models.CharField(max_length=100, blank=True) #우편번호
  address = models.CharField(max_length=100, blank=True) #주소
  extraAddress = models.CharField(max_length=100, blank=True) #세부주소

# class Setting(models.Model):
#   postcode = models.CharField(max_length=100, blank=True) #우편번호
#   address = models.CharField(max_length=100, blank=True) #주소
#   extraAddress = models.CharField(max_length=100, blank=True) #세부주소