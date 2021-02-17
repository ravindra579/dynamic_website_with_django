from django.db import models
from django.utils.timezone import now
# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20)
class interns(models.Model):
	sno=models.AutoField(primary_key=True)
	email=models.ForeignKey('user',on_delete=models.CASCADE)
	company=models.CharField(max_length=50)
	desc=models.TextField()
	field = models.CharField(max_length=20)
class projects(models.Model):
	email=models.ForeignKey('user',on_delete=models.CASCADE)
	desc = models.TextField()
	field = models.CharField(max_length=20)
class job(models.Model):
    email=models.ForeignKey('user',on_delete=models.CASCADE)
    company=models.CharField(max_length=50)
    desc = models.TextField()
    field = models.CharField(max_length=20)
class icomment(models.Model):
    comment=models.TextField()
    user=models.ForeignKey('user', on_delete=models.CASCADE)
    post=models.ForeignKey('interns', on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
class jcomment(models.Model):
    comment=models.TextField()
    user=models.ForeignKey('user', on_delete=models.CASCADE)
    post=models.ForeignKey('job', on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)