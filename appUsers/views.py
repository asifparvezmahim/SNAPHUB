from django.shortcuts import render,redirect
from .forms import Registerform,CustomPasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            messages.success(request,"Successfuly User is Created!!!")
            form.save(commit=True)
            print(form.cleaned_data)
    else:
        form=Registerform()


    return render (request,'regestration_form.html',{'form':form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In!")
                return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect ("home")

@login_required
def profile(request):
    user = request.user
    userPosts = Post.objects.filter(author=user).order_by('-date_time')
    return render (request,"profile.html",{"userPosts":userPosts})
@login_required
def password_change(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully.")
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'password_change_form.html', {'form': form})









