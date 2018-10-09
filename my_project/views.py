from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
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

from .forms import NameForm

def home(request):
    return HttpResponse('Home page !')

def index(request):
    return render(request, 'form.html')

def analyse(request):
    url = request.POST["textfield"]
    print(url)

    res = getInfo(url)

    dump = json.dumps(res)
    return HttpResponse(dump, content_type='application/json')
    #return HttpResponse('Home page !')


def get_html_version(content):
    if content == "html" or content == "HTML" or content == "Doctype HTML" or content == "doctype html" or content == "DOCTYPE HTML" or content == "DOCTYPE html":
        return "HTML 5.0"
    elif content.find("html4")!=-1 or content.find("HTML4")!= -1 or content.find("HTML 4.01")!=-1 or content.find("html 4.01"):
        return "HTML 4.01"
    elif content.find("html3")!=-1 or content.find("HTML3")!= -1 or content.find("HTML 3.2")!=-1 or content.find("html 3.2"):
        return "HTML 3.2"
    elif content.find("html2")!=-1 or content.find("HTML2")!= -1 or content.find("HTML 2.0")!=-1 or content.find("html 2.0"):
        return "HTML 2.0"
    elif content.find("xhtml")!=-1 or content.find("XHTML")!= -1:
        return "XTHML"
    elif content.find("lxml")!=-1 or content.find("LXML")!=-1:
        return "LXML"
    elif content.find("lhtml")!=-1 or content.find("LHTML")!=-1:
        return "LHTML"
    else:
        return "Version Could not be Detected"

def get_heading_info(soup):
    heading = {}

    h1 = soup.findAll("h1")
    h2 = soup.findAll("h2")
    h3 = soup.findAll("h3")
    h4 = soup.findAll("h4")
    h5 = soup.findAll("h5")
    h6 = soup.findAll("h6")

    heading['h1'] = str(len(h1))
    heading['h2'] = str(len(h2))
    heading['h3'] = str(len(h3))
    heading['h4'] = str(len(h4))
    heading['h5'] = str(len(h5))
    heading['h6'] = str(len(h6))

    return heading

def get_forms_info(soup):
    forms = soup.findAll("input")
    count = 0
    for items in forms:
        if items['type']:
            if items['type'] == "password":
                count = count + 1

    if count > 0:
        return True
    else:
        return False

def getInfo(url):

    try:
        #validate = URLValidator()
        #validate(url)
        response = urlopen(url)
        soup = BeautifulSoup(response, "html.parser")
        print(response)
        links = soup.findAll("((http|ftp)s?://.*?)", response)
        print(links)

        #html version of the page
        html_version = get_html_version(soup.contents[0])

        #page title
        page_title = soup.title.string

        # status code : working link
        status_code = 200

        # time_stamp
        time_stamp = str(datetime.datetime.now())

        headings = get_heading_info(soup)

        #login_forms = get_forms_info(soup)
        result = {}
        result['status_code'] = status_code
        result['html_version'] = html_version
        result['page_title'] = page_title
        result['time_stamp'] = time_stamp
        result['headings'] = headings
        #result['login_forms'] = login_forms
        return result

        #return HttpResponse(dump, content_type='application/json')

    except ValidationError:
        print("This link does not work!! Check your link and try again")
