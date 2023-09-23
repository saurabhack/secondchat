from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from .models import Contacts,Signs

# Create your views here.
def home(request):
    obj=Contacts.objects.all()
    return render(request,'home.html',{'obj':obj})

def signup(request):
    if request.method=='POST':
        username=request.POST['name']
        mobile=request.POST['mobile']
        password=request.POST['password']
        password2=request.POST['password2']


        if password==password2:
            if Signs.objects.filter(username=username).exists():
                messages.info(request,'username already used')
                return redirect('login')
            else :
                user=Signs.objects.create(username=username,password=password,mobile=mobile)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password does not matched')
            return redirect('login')
    else:
        return render(request,'signup.html')
def chatbot(request):
    return render(request,'chatbot.html')
def add(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        now=Contacts.objects.create(name=name,phone=phone, user=request.user)
        now.save()
        return redirect('/')
    return render(request,'add.html')
def logi(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        user=auth.authenticate(username=name,mobile=mobile)
        if user !=None:
            auth.login(request,user)
            return redirect('/',{'user':user})
        else:
            messages.info(request,'wrong account')
            return redirect('/')
    else:
        return render(request,'login.html')

def log(request):
    auth.logout(request)
    return redirect('/')
    