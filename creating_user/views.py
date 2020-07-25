from django.shortcuts import render,redirect
from .models import *
#from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def edit(request):
    if request.method =='POST':
        obj = Company_detail()
        if User.objects.filter(username = request.POST['username']).exists() and User.objects.filter(email=request.POST['email']).exists():
            return render(request,'creating_user/page-users-edit.html')
        else:
            user  = User.objects.create_user(username = request.POST['username'],password =request.POST['password'],email=request.POST['email'])
            user.save()
            obj.username = request.POST['username']
            obj.name = request.POST['name']
            obj.email = request.POST['email']
            obj.role_status = request.POST['role']
            obj.status = request.POST['status']
            obj.company_name = request.POST['company']
            company_name = request.POST['company']
            obj.save()
       
            try:
                properties = request.POST['properties']
                Company_detail.objects.filter(company_name=company_name).update(properties_permission = True)
            except:
                pass
            try:
                tenants = request.POST['tenants']
                Company_detail.objects.filter(company_name=company_name).update(tenants_permission = True)
            except:
                pass
            try:
                contacts = request.POST['contacts']
                Company_detail.objects.filter(company_name=company_name).update(contacts_permission = True)
            except:
                pass
            try:
                owners = request.POST['owners']
                Company_detail.objects.filter(company_name=company_name).update(owners_permission = True)
            except:
                pass
        
            return redirect('/')
    else:
        return render(request,'creating_user/page-users-edit.html')

def list(request):
    all_company   = Company_detail.objects.all()
    #context = {'all_company':all_company}
    print(request.user)
    return render(request,'creating_user/page-users-list.html',{'all_company':all_company})

def view(request,pk):
    company = Company_detail.objects.get(pk=pk)


    return render(request,'creating_user/page-users-view.html',{'company':company})
