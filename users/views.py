from django.shortcuts import render
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from bboar.models import Product


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request,user)

                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        "form":form
    }
    return render(request,"users/login.html",context)


def sign_up(request):
    if request.method == "POST":
        form = UserRegistrationForm(data= request.POST)
        if form.is_valid():
            user = form.save (commit=False)
            user.save()

            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserRegistrationForm()
    return render(request,"users/register.html",{"form":form})

def profile(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'users/profile.html', context={"products":products})

    