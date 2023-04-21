from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.template import context,loader
from . forms import SignUpForm,LogInForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

import uuid
from . models import Url

from django.db.models import Count


# Create your views here.





def SignUp(request):
    if request.user.is_authenticated:
        return redirect('shortner:home')
    else:
        if request.method=="POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account has been created successfully !')
        else:
            form = SignUpForm()
        return render(request,'shortner/signup.html',{'form':form})

def LogIn(request):
    if request.user.is_authenticated:
        return redirect('shortner:home')
    else:
        if request.method=="POST":
            form=LogInForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    messages.success(request,"Logged in successfully")
                    return HttpResponseRedirect('/')
        else:
            form = LogInForm()
        return render(request,'shortner/login.html',{'form':form})


@login_required
def Home(request):
    return render(request,'shortner/index.html')


@login_required
def LogOut(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def CreateUrl(request):
        if request.method=="POST":
            url = request.POST.get('url')
            if Url.objects.filter(url=url,user=request.user).exists():
                record = Url.objects.get(url=url,user=request.user)
                context ={"data":record.uuid}
                record.increase_topSearched()
            else:
                uid = str(uuid.uuid4())[:10]
                url = Url(user=request.user,url=url,uuid=uid)
                context ={"data":uid}
                url.save()
            template = loader.get_template('shortner/card.html')
            card = template.render(context)
            return HttpResponse(card)

@login_required
def Jump(request,pk):
     url =  Url.objects.get(uuid=pk)
     return redirect(f"https://{url.url}")

@login_required
def Profile(request):
    userData = Url.objects.filter(user=request.user)
    mostVisited = Url.objects.filter(user=request.user).annotate(count=Count('topSearched')).order_by('-topSearched')
    
    return render(request,'shortner/profile.html',{"userData":userData,"mostVisited":mostVisited})

@login_required
def DeleteUrl(request,pk):
    url = Url.objects.get(id=pk)
    url.delete()
    return redirect('shortner:profile')

     
