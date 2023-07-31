from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')

        if get_password != get_confirm_password:
            messages.info(request, "Passwords doesn't match")
            return redirect('signup_page')
        
        try:
            if User.objects.get(username=get_email):
                messages.warning(request, 'Email already registered')
                return redirect('signup_page')
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(get_email, get_email, get_password)
        myuser.save()
        messages.success(request, 'User Successfully created! Please Login')
        return redirect('login_page')
    return render(request, 'signup.html')


def handle_login(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        myuser = authenticate(username=get_email, password=get_password)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful!")
            return redirect('/')
        else:
            messages.error(request, "Username or Password ddoesn't match")
    

    return render(request, 'login.html')

def handle_logout(request):
    logout(request)
    messages.success(request, "Logout Successful!")
    return render(request, 'login.html')