from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User,auth
from django.contrib import messages
from creating_user.models import *



def signup(request):
    '''
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():
            print('username is taken')
            return redirect('auth-register')
        elif User.objects.filter(email=email).exists():
            print('email is taken')
            return redirect('auth-register')
        else:
            user  = User.objects.create_user(username = username,password = password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('user successfully created')
            return redirect('auth-login')

    else:  

    '''    

    return render (request,'account/signup.html')


def login(request):
    
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

       

        user = auth.authenticate(username=username,password=password)
        #req = request.user.username
        #print(req)

        com_obj = Company_detail.objects.get(username=username)
        print(com_obj.properties_permission)

        

        if user is not None:
            auth.login(request, user)
            return render(request,'home.html',{'com_obj':com_obj})
        else:
            print('login failed')
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
     
        return render(request,'account/login.html')



def logout(request):
    auth.logout(request)
    return redirect('login')

   