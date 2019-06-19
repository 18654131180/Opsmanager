from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from cmdb.models import  *
from django.http import JsonResponse
from fabric.api import *
from fabric.tasks import execute
from datetime import datetime

env.hosts = ['192.168.182.140']  # 指定 hosts 远程主机
# env.key_filename = '/c/Users/Administrator/.ssh/id_rsa'     # 指定你的私钥文件
# 指定用户名
env.user = 'root'
env.password = '123456'
def pack():
    """打包文件"""
    tag = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    basedir = "/tmp/www.txt"
    run('tar zcvf {0}_{1}.tar.gz {2}'.format(basedir, tag, basedir))

@login_required
def index(request):
    '''默认主页，显示发布页面'''
    companys = Company.objects.all()
    context = {"companys": companys}
    return render(request, 'deploy/deploy_test.html', context)

@login_required
def deploy(request):
    if request.method=="GET":
        return render(request,'deploy/deploy_test.html')
    elif request.method=="POST":
        execute(pack)
        # pack()
        context={"status":200,"message":"ok"}
        return JsonResponse(context)

@login_required
def detail_company(request,company_id):
    '''显示公司下的服务器'''
    servers = Servers.objects.filter(company_id=company_id)
    context = {"servers": servers}
    return render(request, 'deploy/deploy_server_detail.html', context)
