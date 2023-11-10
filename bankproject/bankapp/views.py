from django.shortcuts import render,redirect

import bankapp
from .forms import CustForm
from .models import Customer,Branch
from django.contrib import messages
app_name=bankapp

# Create your views here.
def home(request):
    return render(request,'index.html')
def new(request):
    return render(request,'new.html')
# def custreg(request):
#     return render(request,'customer.html')
def customer_create_view(request):
    form=CustForm()
    if request.method=='POST':
        # CustForm.request_change=True
        form=CustForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Application submit successfully")
            # form=CustForm()
            # return redirect('add/')

    return render(request,'customer.html',{'form':form})


# Ajax
def load_branches(request):
    district_id=request.GET.get('District_id')
    branchs=Branch.objects.filter(District_id=district_id).all()
    return render(request,'branch_list_options.html',{'branchs':branchs})
