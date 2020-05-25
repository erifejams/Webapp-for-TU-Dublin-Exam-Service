from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
	
# Create your views here.
def index(request):
# This method uses the page request to determine which page to return
    # create context
    context = {}
    pagereq=str(request.path)

    if "index" in pagereq:
        return render(request,'index.html',context)
    else:
        return render(request,'404.html',context)


def index2(request):
# This method uses the page request to determine which page to return
    # create context
    context = {}
    pagereq=str(request.path)

    if "index2" in pagereq:
        return render(request,'index2.html',context)
    else:
        return render(request,'404.html',context)


def index3(request):
# This method uses the page request to determine which page to return
    # create context
    context = {}
    pagereq=str(request.path)

    if "index" in pagereq:
        return render(request,'index3.html',context)
    else:
        return render(request,'404.html',context)