from django.contrib.auth.forms import UserCreationForm #상속받기
from .models import CustomUser

class RegisterForm(UserCreationForm): #class상속

  class Meta:
    model= CustomUser
    fields= ['username','password1','password2','gender']