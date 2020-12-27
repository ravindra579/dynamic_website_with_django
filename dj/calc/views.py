from django.shortcuts import render
from django.http import HttpResponse
from calc.models import user,projects,job,intern,save
# Create your views here.
def home(request):
    return render(request,'html.html')
def signup(request):
    return render(request,'signup.html')
def login(request):
    uid=1
    name=request.POST["name"]
    email=request.POST["email"]
    password=request.POST["pass"]
    userss=user(uid=uid,name=name,email=email,password=password)
    userss.save()
    return render(request,'login.html')
def login1(request):
    return render(request,'login.html')
def c(request):
    return render(request,'html1.html')
def html1(request):
    emil=request.POST["emil"]
    passw=request.POST["pass2"] 
    try:
        userr=user.objects.get(email=emil)
    except:
        userr=None
    try:
        p=user.objects.get(password=passw)
    except:
        p=None
    save.email=emil
    if(userr is not None and p is not None):
        return render(request,'html1.html')
    else:
        return render(request,'login.html')
    
def account(request):
    data=user.objects.filter(email=save.email)
    context={}
    context["dataset"]=data
    return render(request,"account.html",context)
def logout(request):
    return render(request,'logout.html')
def project(request):
    detail=user.objects.filter(email=save.email)
    details=projects.objects.all()
    context={}
    context["dataset"]=details
    return render(request,'project.html',context)
def internh(request):
    detail=user.objects.filter(email=save.email)
    details=intern.objects.all()
    context={}
    context["dataset"]=details
    return render(request,'intern.html',context)
def jobh(request):
    detail=user.objects.filter(email=save.email)
    details=job.objects.all()
    context={}
    context["dataset"]=details
    return render(request,'job.html',context)
def new(request):
    #data=user.objects.filter(email=save.email)
    detail=user.objects.filter(email=save.email)
    details=intern.objects.filter(uid=3)
    context={}
    context["dataset"]=details
    return render(request,"new.html",context)
def new1(request):
    #data=user.objects.filter(email=save.email)
    detail=user.objects.filter(email=save.email)
    details=projects.objects.filter(uid=3)
    context={}
    context["dataset"]=details
    return render(request,"new1.html",context)
def new2(request):
    #data=user.objects.filter(email=save.email)
    detail=user.objects.filter(email=save.email)
    details=job.objects.filter(uid=3)
    context={}
    context["dataset"]=details
    return render(request,"new2.html",context)
def newi(request):
    field=request.POST["field"]
    desc=request.POST["desc"] 
    #data=user.objects.filter(email=save.email)
    detail=user.objects.filter(email=save.email)
    if(field != " "):
     intern.objects.filter(uid=3).update(field=field)
    if(desc != " "):
     intern.objects.filter(uid=3).update(desc=desc)
    details=intern.objects.filter(uid=3)
    context={}
    context["dataset"]=details
    return render(request,"new.html",context)
def newp(request):
    field=request.POST["field"]
    desc=request.POST["desc"] 
    #data=user.objects.filter(email=save.email)
    detail=user.objects.filter(email=save.email)
    if(field != " "):
     projects.objects.filter(uid=3).update(field=field)
    if(desc != " "):
     projects.objects.filter(uid=3).update(desc=desc)
    details=projects.objects.filter(uid=3)
    context={}
    context["dataset"]=details
    return render(request,"new1.html",context)
def newj(request):
    field=request.POST["field"]
    desc=request.POST["desc"] 
    #data=user.objects.filter(email=save.email)
    detail=user.objects.filter(email=save.email)
    if(field != " "):
     job.objects.filter(uid=3).update(field=field)
    if(desc != " "):
     job.objects.filter(uid=3).update(desc=desc)
    details=job.objects.filter(uid=3)
    context={}
    context["dataset"]=details
    return render(request,"new2.html",context)