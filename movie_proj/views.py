from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required 
def homeView(request):
    date_today = datetime.now().date()
    print('Date Doday ', datetime.now().date())
    print('DateTime ', datetime.now())
    return render(request,'main/home.html',{'date_today':date_today})


def loginView(request):
    error_message = None
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_director == False:
            login(request,user)
            
            #!login_required part yeni istifadecinin griis edib etmemeyine gore
            if request.GET.get('next'):
                print(request.GET.get('next'))
                return redirect(request.GET.get('next'))
            else:
                return redirect('homeView')
        else:
            error_message = 'Ups something went wrong.Are you sure you are a producer?'
            #####################################
    return render(request,'main/login.html',{'form':form,'error_message':error_message})

def logoutView(request):
    logout(request)
    return redirect('logoutView')