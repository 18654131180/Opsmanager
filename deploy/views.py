from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from cmdb.models import  *
from django.http import JsonResponse



@login_required
def index(request):
    '''默认主页，显示发布页面'''
    companys = Company.objects.all()
    context = {"companys": companys}
    return render(request, 'deploy/deploy.html', context)

@login_required
def detail_company(request,company_id):
    '''显示公司下的服务器'''
    servers = Servers.objects.filter(company_id=company_id)
    context = {"servers": servers}
    return render(request, 'deploy/deploy_server_detail.html', context)
