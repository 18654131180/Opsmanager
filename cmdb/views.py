from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *
from dateutil.parser import parse
import time
daytime=time.strftime('%Y-%m-%d',time.localtime(time.time()))

@login_required
def index(request):
    '''默认主页，显示公司'''
    companys = Company.objects.all()
    context = {"companys": companys}
    return render(request, 'cmdb/index.html', context)


@login_required
def showcompanys(request):
    '''显示公司'''
    companys = Company.objects.all()
    context = {"companys": companys}
    return render(request, 'cmdb/index.html', context)


@login_required
def show_company(request,company_id):
    '''显示公司下的服务器'''
    servers = Servers.objects.filter(company_id=company_id)
    context = {"servers": servers}
    return render(request, 'cmdb/server_detail.html', context)

@login_required
def edit_company(request, company_id):
    """实现编辑公司"""
    company = Company.objects.get(id=company_id)
    if request.method != "POST":
        form = CompanyForm(instance=company)
    else:
        form = CompanyForm(instance=company, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cmdb:company'))
    context = {"company": company, "form": form}
    return render(request, 'cmdb/edit_company.html', context)


@login_required
def new_company(request):
    """添加新主题"""
    if request.method != 'POST':
        form = CompanyForm
    else:
        form = CompanyForm(request.POST)
        if form.is_valid():
            # new_company=form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('cmdb:company'))  # 通过appname加上urls.py定义的name得到url
    context = {'form': form}
    return render(request, 'cmdb/new_company.html', context)


@login_required
def del_company(request, company_id):
    """删除公司"""
    delcompany = Company.objects.get(id=company_id).delete()
    if delcompany:
        return HttpResponseRedirect(reverse('cmdb:company'))
    context = {"delcopany": delcompany}
    return render(request, 'cmdb/index.html', context)

@login_required
def showservers(request):
    '''显示服务器信息'''
    servers = Servers.objects.all()
    daytime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    context = {"servers": servers,'daytime':daytime}
    return render(request, 'cmdb/server.html', context)



@login_required
def edit_server(request, server_id):
    """实现编辑公司"""
    server = Servers.objects.get(id=server_id)
    if request.method != "POST":
        form = ServerForm(instance=server)
    else:
        form = ServerForm(instance=server, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cmdb:server'))
    context = {"server": server, "form": form}
    return render(request, 'cmdb/edit_server.html', context)

@login_required
def new_server(request):
    """添加服务器"""
    if request.method != 'POST':
        form = ServerForm
    else:
        form = ServerForm(request.POST)
        if form.is_valid():
            # new_company=form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('cmdb:server'))  # 通过appname加上urls.py定义的name得到url
    context = {'form': form}
    return render(request, 'cmdb/new_server.html', context)


@login_required
def del_server(request, server_id):
    """删除服务器"""
    delserver = Company.objects.get(id=server_id).delete()
    if delserver:
        return HttpResponseRedirect(reverse('cmdb:server'))
    context = {"delserver": delserver}
    return render(request, 'cmdb/server.html', context)