from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
import sys
import argparse
import json
import pprint
import re
import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests
from bs4 import BeautifulSoup, Doctype
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from .forms import Form
from rest_framework import viewsets
from .models import Webpage
import ssl
from urllib.parse import urlparse
from . import scrapingHelper
from django.core.cache import cache


def home(request):
    return HttpResponse('Home page !')

def index(request):
    return render(request, 'form.html')

def analyse(request):
    if request.method == "POST":
        address = request.POST.get('address')
        form = Form(request.POST)
        if form.is_valid():
            if cache.get(address) is not None:
                resultString = cache.get(address)
                print('cache found')
            else:
                resultObjInitial = scrapingHelper.getInfo(address)
                resultString = str(resultObjInitial)
                cache.set(address, resultString, 60)
                
            resultObj = Webpage()
            resultStringAttr = resultString.split("~")
            print(resultStringAttr)
            resultObj.address = resultStringAttr[0]
            resultObj.errorType = int(resultStringAttr[1])
            resultObj.h1Count = int(resultStringAttr[2])
            resultObj.h2Count = int(resultStringAttr[3])
            resultObj.h3Count = int(resultStringAttr[4])
            resultObj.h4Count = int(resultStringAttr[5])
            resultObj.h5Count = int(resultStringAttr[6])
            resultObj.h6Count = int(resultStringAttr[7])
            resultObj.version = resultStringAttr[8]
            resultObj.internalLinkCount = int(resultStringAttr[9])
            resultObj.externalLinkCount = int(resultStringAttr[10])
            resultObj.inaccessibleLinkCount = int(resultStringAttr[11])
            resultObj.statusCode = int(resultStringAttr[12])
            resultObj.timeStamp = resultStringAttr[13]
            resultObj.loginForm = bool(resultStringAttr[14])
            resultObj.errorMessage = resultStringAttr[15]

            context = {
                "webpage":resultObj
            }
            if resultObj.errorType == 0:
                return render(request, 'result.html', context)
            elif resultObj.errorType == 1:
                return render(request, 'resultHTTPError.html', context)
            elif resultObj.errorType == 2:
                return render(request, 'resultURLError.html', context)
            else:
                return render(request, 'resultInvalidURL.html', context)
    else:
        form = Form()
    context = {
        "form":form
    }
    return render(request, "form.html", context)