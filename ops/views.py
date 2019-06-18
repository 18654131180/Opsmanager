from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import  *


def index(request):
    return render(request,'ops/index.html')

@login_required
def deploy(request):
    if request.method == "GET":
        return render()