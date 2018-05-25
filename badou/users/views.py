from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.urls import reverse

from .models import User
from .forms import RegisterForm, LoginForm
from .backends import MobileBackend


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            # form.clean_password2()
            form.save()
            messages.success(request, '注册成功，请登录！')
            return redirect(reverse('login'))
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def person_center(request):
    if request.user.is_authenticated():
        mobile = request.user.mobile
        return render(request, 'me.html', {'mobile': mobile})
    else:
        return redirect(reverse('login'))


def hello(request,pk):
    user = get_object_or_404(User, mobile=pk)
    print("________")
    print(user.mobile)
    return render(request,'hello.html',locals())


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        mobile = form.data.get("mobile")
        password = request.POST.get('password')
        user = MobileBackend.authenticate(mobile=mobile, password=password)
        if user:
            return redirect(reverse('hello', kwargs={'pk': user.mobile}))
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
