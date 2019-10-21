from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
# # Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         print("check")
#         if form.is_valid():
#             print("valid")
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             # return redirect('')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})
# def profile(request):
#     return render(request, 'users/profile.html')
#
# def login(request):
#     return render(request, 'users/login.html')

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, UserRegisterForm
def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user:
            login(request, user)
            return redirect('../weather/')
        else:
            context['error'] = "Porvide valide credentials"
            return render(request, "users/login.html", context)
        pass
    else:
        return render(request, "users/login.html", context)
def profile_user(request):
     return render(request, 'users/profile.html')

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return(HttpResponseRedirect(reverse('login_user')))
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['repassword']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Username exists")
            elif User.objects.filter(email=email).exists():
                print("email taken")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                context = {}
                return render(request, "users/login.html", context)
        else:
            return render(request, 'users/register.html')

    else:
        return render(request, 'users/register.html')
