from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('login1',views.login1,name='login1'),
    path('html',views.home,name='home'),
    path('c',views.c,name='c'),
    path('html1',views.html1,name='html1'),
    path('account',views.account,name='home'),
    path('logout',views.logout,name='logout'),
    path('intern',views.internh,name='intern'),
    path('project',views.project,name='project'),
    path('job',views.jobh,name='jobs'),
    path('new',views.new,name='new'),
    path('newi',views.newi,name='newi'),
    path('new1',views.new1,name='new1'),
    path('new2',views.new2,name='new2'),
    path('newp',views.newi,name='newp'),
    path('newj',views.newi,name='newj')
]