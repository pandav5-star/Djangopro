from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            request.session['username']=username
            return HttpResponse ('Loggerd in successfully')
        else:
            return HttpResponse('Invalid username or password') 

    return render(request,'user/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        my_user = User.objects.create_user(username,email,password)
        my_user.save()

       # mention url name here 
        return redirect('login')
    return render(request,'user/signup.html')


def user_logout(request):
    logout(request)
    return redirect('login')