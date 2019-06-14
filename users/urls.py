#coding:utf-8
"""定义learning_logs的URL Patterns"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views


urlpatterns = [
	#用户登录
	url(r'^login',login,{'template_name':'users/login.html'},name='login'),
	#用户退出
	url(r'^logout',views.logout_view,name='logout'),
	#用户注册
	url(r"^register/$",views.register,name='register')
]
