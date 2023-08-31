from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
from account.models import User
from django.contrib.auth import authenticate, login, logout
from . decorators import login_required
from django.contrib import messages
from django.contrib import auth


def login(request):
    try:
        if request.user.is_authenticated:
            return render(request,'dashboard/index.html')

        if request.method =="POST":
            email = request.POST['useremail']
            print(email)
            password = request.POST['password']
            user_obj = User.objects.filter(email= email)
            if not user_obj.exists():
                messages.warning(request,"Invalid username...")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                
            
            user_obj = authenticate(email=email, password=password)
            if user_obj and user_obj.is_admin:
                auth.login(request, user_obj)
                return redirect('dashboard:index')
            
            messages.warning(request,'Inavlid Password')
            return redirect('dashboard:login')
            
        return render(request,'dashboard/login.html')
            

    except Exception as e:
        print(e)
        messages.warning(request,'something wrong...')
        return redirect('dashboard:login')


@login_required
def userlogout(request):
    auth.logout(request)
    messages.info(request,"logout successfully..")
    return redirect('dashboard:login')


@login_required
def index(request):
    return render(request,'dashboard/index.html')

@login_required
def addCategories(request):
    active = True
    return render(request,'dashboard/addCategories.html',{'active':active})

@login_required
def addProduct(request):
    active = True
    return render(request,'dashboard/create-post.html',{'active':active})


@login_required
def orderList(request):
    orderactive = True
    return render(request,'dashboard/datatables.html', {'orderactive':orderactive})

@login_required
def agentList(request):
    agent_active = True
    return render(request,'dashboard/agentList.html', {'agent_active':agent_active})


@login_required
def userList(request):
    user_active = True
    return render(request,'dashboard/userlist.html',{'user_active':user_active})

@login_required
def inboxEmail(request):
    return render(request,'dashboard/inbox-email.html')

@login_required
def composeEmail(request):
    return render(request,'dashboard/composeEmail.html')

@login_required
def readEmail(request):
    return render(request,'dashboard/email-read.html')