from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tasks,TaskCategory,CheckPoints
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewForm
# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"category":TaskCategory.objects.all()}
                 )

def slug(request,single_slug):
    categories=[c.category_slug for c in TaskCategory.objects.all()]
    if single_slug in categories:
        matching_task = CheckPoints.objects.filter(task_category__category_slug=single_slug)
        series_url = {}
        for m in matching_task.all():
            first=Tasks.objects.filter(task_checkpoint__task_checkpoint=m.task_checkpoint)
            series_url[m] = first
        return render(request,"main/category.html",{"first_p":series_url})
    
    tasks=[t.task_slug for t in Tasks.objects.all()]
    if single_slug in tasks:
        return HttpResponse(f"{single_slug} is the category")
    
    return HttpResponse(f"{single_slug} dosent exist")

def register(request):
    if request.method == "POST":
        form=NewForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Account created : {username}")
            login(request,user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])

    form = NewForm
    return render(request,"main/register.html",context={"form":form})      

def logout_req(request):
    logout(request)
    messages.info(request,'Logout successfull..!')
    return redirect("main:homepage")

def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"Logged in as {username}")
                return redirect("main:homepage")

    

    form = AuthenticationForm()
    return render(request,"main/login.html",context={"form":form})