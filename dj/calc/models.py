from django.db import models

# Create your models here.
class user(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    def name_(self):
        return [name for name in user._meta.name]
    def email_(self):
        return user.email
    def password_(self):
        return user.password
    def uid_(self):
        return user.uid
class intern(models.Model):
    uid = models.IntegerField()
    desc = models.TextField()
    field = models.CharField(max_length=20)
class projects(models.Model):
    uid = models.IntegerField()
    desc = models.TextField()
    field = models.CharField(max_length=20)
class job(models.Model):
    uid = models.BigIntegerField()
    desc = models.TextField()
    field = models.CharField(max_length=20)
class save(models.Model):
    email = models.CharField(max_length=20)