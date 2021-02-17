
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from calc.models import user,projects,job,interns,icomment,jcomment
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def home(request):
    return render(request,'html.html')
def signup(request):
    return render(request,'signup.html')
@csrf_protect
def login(request):
    name=request.POST["name"]
    email=request.POST["email"]
    password=request.POST["pass"]
    userss=user(name=name,email=email,password=password)
    userss.save()
    return render(request,'login.html')
def login1(request):
    return render(request,'login.html')
def html1(request):
    emil=request.POST["emil"]
    passw=request.POST["pass2"] 
    try:
        userr=user.objects.get(email=emil)
        inter=interns.objects.all()
        jo=job.objects.all()
        request.session['email'] = emil
        icom=icomment.objects.all()
        jcom=jcomment.objects.all()
        #n=icom.count()
    except:
        userr=None
    try:
        p=user.objects.get(password=passw)
    except:
        p=None
    if(userr is not None and p is not None and userr.password==passw):
        return render(request,'html1.html',{'data':userr,'inter':inter,'jo':jo,'com':icom,'jcom':jcom})
    else:
        return render(request,'login.html',{'error':'**Wrong crendentials'})
    
def account(request):
    data=user.objects.get(email=request.session['email'])
    if(interns.objects.filter(email=data).exists()):
      inter=interns.objects.get(email=data)
      icom=icomment.objects.filter(post=inter)
      icommen=icomment.objects.filter(user=data)
      i=1
    else:
      i=0
    if(job.objects.filter(email=data).exists()):
      jo=job.objects.get(email=data)
      jcom=jcomment.objects.filter(post=jo)
      jcommen=jcomment.objects.filter(user=data)
      j=1
    else:
      j=0
    if(i==0 and j==0):
      return render(request,"account.html",{'data':data})
    if(i==1 and j==1):
      return render(request,"account.html",{'data':data,'inter':inter,'jo':jo,'com':icom,'jcom':jcom,'icommen':icommen,'jcommen':jcommen})
    else:
      if(i==1):
        return render(request,"account.html",{'data':data,'inter':inter,'com':icom,'icommen':icommen})
      else:
        return render(request,"account.html",{'data':data,'jo':jo,'jcom':jcom,'jcommen':jcommen})
def logout(request):
    return render(request,'logout.html')
def new(request):
    data=user.objects.get(email=request.session['email'])
    if(interns.objects.filter(email=data).exists()):
      inter=interns.objects.get(email=data)
      icom=icomment.objects.filter(post=inter)
      icommen=icomment.objects.filter(user=data)
      i=1
    else:
      i=0
    if(job.objects.filter(email=data).exists()):
      jo=job.objects.get(email=data)
      jcom=jcomment.objects.filter(post=jo)
      jcommen=jcomment.objects.filter(user=data)
      j=1
    else:
      j=0
    if(i==0 and j==0):
      return render(request,"account.html",{'data':data})
    if(i==1 and j==1):
      return render(request,"account.html",{'data':data,'inter':inter,'jo':jo,'com':icom,'jcom':jcom,'icommen':icommen,'jcommen':jcommen})
    else:
      if(i==1):
        return render(request,"account.html",{'data':data,'inter':inter,'com':icom,'icommen':icommen})
      else:
        return render(request,"account.html",{'data':data,'jo':jo,'jcom':jcom,'jcommen':jcommen})
def newi(request):
    try:
        fiel=request.POST["field"]
        des=request.POST["desc"] 
        comp=request.POST["company"]
        if(interns.objects.filter(email=user.objects.get(email=request.session['email'])).exists()):
         inter=interns.objects.get(email=user.objects.get(email=request.session['email']))
         inter.field=fiel
         inter.email=user.objects.get(email=request.session['email'])
         inter.company=comp
         inter.desc=des
         inter.save()
        else:  
         fiel=request.POST["field"]
         des=request.POST["desc"] 
         comp=request.POST["company"]
         data=user.objects.get(email=request.session['email'])
         inter=interns(email=data,company=comp,desc=des,field=fiel)
         inter.save()

    finally:
        return redirect('new')
def newj(request):
    try:
        fiel=request.POST["fieldj"]
        des=request.POST["descj"] 
        comp=request.POST["companyj"]
        if(job.objects.filter(email=user.objects.get(email=request.session['email'])).exists()):
            inter=job.objects.get(email=user.objects.get(email=request.session['email']))
            inter.field=fiel
            inter.email=user.objects.get(email=request.session['email'])
            inter.company=comp
            inter.desc=des
            inter.save()
        else:
         fiel=request.POST["fieldj"]
         des=request.POST["descj"] 
         comp=request.POST["companyj"]
         data=user.objects.get(email=request.session['email'])
         inter=job(email=data,company=comp,desc=des,field=fiel)
         inter.save()			
    finally:
        return redirect('new')
def postComment(request):
	try:
		commen=request.POST["use"]
		usr=user.objects.get(email=commen)
		pos=request.POST["postSno"]
		comment=request.POST["comment"]
		postSno=interns.objects.get(email=user.objects.get(email=pos))
		comment=icomment(comment= comment, user=usr, post=postSno)
		comment.save()
	finally:
	    return redirect('comment')
def jpostComment(request):
	try:
		commen=request.POST["use"]
		usr=user.objects.get(email=commen)
		pos=request.POST["postSno"]
		comment=request.POST["comment"]
		postSno=job.objects.get(email=user.objects.get(email=pos))
		comment=jcomment(comment= comment, user=usr, post=postSno)
		comment.save()
	finally:
	    return redirect('comment')
def comment(request):
	userr=user.objects.get(email=request.session['email'])
	inter=interns.objects.all() 
	icom=icomment.objects.all()
    #n=icom.count() 
	jo=job.objects.all()
	jcom=jcomment.objects.all()
	return render(request,'html1.html',{'data':userr,'inter':inter,'jo':jo,'com':icom,'jcom':jcom})
def delet(request):
	a=request.POST["a"]
	icomment.objects.get(id=a).delete()
	return redirect('new')
def deletj(request):
	a=request.POST["b"]
	jcomment.objects.get(id=a).delete()
	return redirect('new')
def filter(request):
	return render(request,'filter.html')
def filtera(request):
	a=request.POST.getlist('checks[]')
	k=0
	l=0
	print(a)
	inter=interns.objects.all()
	jo=job.objects.all()
	m=0
	for i in range(len(a)):
		if(a[i]=='internship'):
			k=1
		if(a[i]=='job'):
			l=1
		if(a[i]!='job' and a[i]!='internship' and m==0):
			inter=interns.objects.filter(field=a[i])
			jo=job.objects.filter(field=a[i])
			m=1
		if(a[i]!='job' and a[i]!='internship'):
			inter=inter | interns.objects.filter(field=a[i])
			jo=jo | job.objects.filter(field=a[i])
	userr=user.objects.get(email=request.session['email'])
	icom=icomment.objects.all()
	jcom=jcomment.objects.all()
	if((k==0 and l==0) or (k==1 and l==1)):
	  return render(request,'html1.html',{'data':userr,'inter':inter,'jo':jo,'com':icom,'jcom':jcom,'filter':"Filter"})
	else:
	  if(k==1):
           return render(request,'html1.html',{'data':userr,'inter':inter,'com':icom,'filter':"Filter"})
	  else:
           return render(request,'html1.html',{'data':userr,'jo':jo,'jcom':jcom,'filter':"Filter"})
