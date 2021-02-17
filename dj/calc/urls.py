from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('login1',views.login1,name='login1'),
    path('html',views.home,name='home'),
    path('html1',views.html1,name='html1'),
    path('account',views.account,name='home'),
    path('logout',views.logout,name='logout'),
    path('new',views.new,name='new'),
	path('newi',views.newi,name='newi'),
	path('delet',views.delet,name='delet'),
	path('deletj',views.deletj,name='deletj'),
	path('newj',views.newj,name='newj'),
	path('filter',views.filter,name='filter'),
	path('filtera',views.filtera,name='filtera'),
	path('postComment', views.postComment, name="postComment"),
	path('jpostComment', views.jpostComment, name="jpostComment"),
	path('comment', views.comment, name="comment")
]