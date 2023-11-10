from django.shortcuts import render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
import credentials_app
app_name=credentials_app
# Create your views here.

#login
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            # return render(request,'new.html')
            return render(request,'new.html')
        else:
            messages.info(request, "Invalid credentials")
            return render(request,'login.html')

    else:
        return render(request,'login.html')



# Register

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpwd=request.POST['password1']
        if password==cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return render(request,'register.html')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return render(request,'login.html')
        else:
            messages.info(request,'Password not matching')
            return render(request,'register.html')
    else:
        return render(request,'register.html')
            


# logout
def logout(request):
    auth.logout(request)
    return render(request,'index.html')

