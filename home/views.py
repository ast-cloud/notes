from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from home.models import Notetable
from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    allnotes=Notetable.objects.filter(userid=request.user.username)
    output={}
    l=len(list(allnotes))
    color=[('white','primary'),('white','secondary'),('white','success'),('white','warning'),('white','danger'),('white','info'),('dark','light'),('white','dark')]
    for i,a in enumerate(allnotes):
        output['data'+str(i)]={}
        output['data'+str(i)]['note']=a.note
        output['data'+str(i)]['dt']=a.dt.strftime('%#I:%M %p %#d %B, %Y')
        output['data'+str(i)]['txt']=color[i%8][0]
        output['data'+str(i)]['bg']=color[i%8][1]
        output['data'+str(i)]['nid']=a.id

    od={'info':output,'length':l}
    return render(request, 'index.html', od)

def newnote(request):
    if request.method=='POST':
        note=request.POST.get('note')
        userid=request.user.username
        notetable=Notetable(note=note, userid=userid, dt=datetime.today())
        notetable.save()
        return redirect('/')
    
    return render(request, 'newnote.html') 

def delnote(request, nid):
    if request.method=='GET':
        Notetable.objects.filter(id=nid).delete()
    return redirect('/')

def editnote(request,nid):
    if request.method=='GET':
        editdata=Notetable.objects.filter(id=nid)
        datadict={'note':editdata[0].note,'nid':editdata[0].id}
        return render(request, 'editnote.html', datadict) 
    
    if request.method=='POST':
        a=Notetable.objects.get(id=nid)
        a.note=request.POST.get('note')
        a.save()
        return redirect('/')

def loginuser(request):
    if request.method=='POST':
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        usr=authenticate(username=un, password=pswd)
 
        if usr is not None:
            login(request, usr)
            return redirect('/')
            
        else:
            messages.error(request, 'Wrong username or password!')
            
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        postedusername=request.POST.get('username')
        User=get_user_model()
        all=User.objects.all()
        unique=True
        for a in all:
            if str(a)==postedusername:
                unique=False
                break

        if unique==False:    
            messages.error(request,'Username already exists.')
            return render(request, 'signup.html')
        else:
            postedpassword=request.POST.get('password')
            newuser=User(username=postedusername)
            newuser.set_password(postedpassword)
            newuser.save()
            messages.success(request, 'Account created successfully. Please login now!')
            return redirect('/')

    return render(request, 'signup.html')
    


def logoutuser(request):
    logout(request)
    return redirect('/login')