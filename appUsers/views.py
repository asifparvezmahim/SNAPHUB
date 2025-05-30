from django.shortcuts import render,redirect
from .forms import Registerform
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

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
    return redirect ("user_login")
def profile(request):
    return render (request,"profile.html")






