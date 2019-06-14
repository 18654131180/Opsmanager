from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import  *
from .forms import *



@login_required
def index(request):
    companys=Company.objects.all()
    context={"companys":companys}
    return render(request,'cmdb/index.html',context)

@login_required
def showcompanys(request):
    companys = Company.objects.all()
    context = {"companys": companys}
    return render(request, 'cmdb/index.html', context)

@login_required
def showservers(request):
    servers = Servers.objects.all()
    context = {"servers": servers}
    return render(request, 'cmdb/server.html', context)

@login_required
def edit_company(request,company_id):
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

