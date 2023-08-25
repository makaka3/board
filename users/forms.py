from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Введите имя пользователя","class":"form-control custom"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Введите пароль","class":"form-control custom"}))
    class Meta:
        model = User
        fileds= ('username','password')
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]