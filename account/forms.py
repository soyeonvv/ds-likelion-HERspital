from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #상속받기
from .models import CustomUser
from django.contrib.auth.hashers import check_password
from django import forms

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm): #class상속

  class Meta:
    model= CustomUser
    fields= ['username','password','password2','gender']
  

class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control',}), 
    )
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
    fields= ['username','password','password2','nickname','email','birth','gender','position','certifyImg','workplace'
      ,'postcode','address','extraAddress'
    ]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['postcode','address','extraAddress']