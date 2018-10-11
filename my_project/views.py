from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import Form
from . import scrapingHelper
from django.core.cache import cache


def home(request):
    return HttpResponse('WELCOME TO THE URL Analyser App')


def index(request):
    return render(request, 'form.html')


def analyse(request):
    if request.method == "POST":
        address = request.POST.get('address')
        form = Form(request.POST)
        if form.is_valid():
            if cache.get(address) is not None:
                result_object = cache.get(address)
                print('cache found')
            else:
                result_object = scrapingHelper.get_info(address)
            context = {
                "webpage":result_object
            }
            if result_object.errorType == 0:
                # Setting up the cache for 24 hours
                cache.set(address, result_object, 60*60*24)
                return render(request, 'result.html', context)
            elif result_object.errorType == 1:
                return render(request, 'resultHTTPError.html', context)
            elif result_object.errorType == 2:
                return render(request, 'resultURLError.html', context)
            else:
                return render(request, 'resultInvalidURL.html', context)
    else:
        form = Form()
    context = {
        "form":form
    }
    return render(request, "form.html", context)
