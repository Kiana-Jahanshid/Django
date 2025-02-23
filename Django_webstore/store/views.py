from django.shortcuts import render , redirect 
from .forms import SignInForm , SignUpForm , AuthenticationForm
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required 
from django.urls import reverse
from django.contrib import messages


def index(request):
    return render(request , template_name="index.html")

def products(request):
    return render(request , template_name="products.html")

def elements(request):
    return render(request , template_name="elements.html")

def signupView(request):
    if request.method == "GET":
        form = SignUpForm()

    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user) # after signingup , it will automatically signin  
            return redirect("/signin/")

    return render(request , template_name="signup.html" , context={'form': form})



def signinView(request):
    if request.method == "GET":
        form = SignInForm()

    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user) # after signingup , it will automatically signin  
            if user is not None :
                messages.success(request , "You have successfully logged in ✔ ")
                return redirect("/profile/")
            else :
                messages.error(request , "Invalid username or password ❌") 
                
    return render(request , template_name="signin.html" , context={'form': form})


def signoutView(request):
    logout(request)
    return render(request , template_name="index.html")

@login_required
def profileView(request):
    return render(request , template_name="profile.html" , context={"user":request.user}) 
