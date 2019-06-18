from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import  *
from django.http import JsonResponse


def index(request):
    return render(request,'ops/index.html')
