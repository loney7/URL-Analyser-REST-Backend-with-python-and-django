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

def get_html_version(content):
    if content == "html" or content == "HTML" or content == "Doctype HTML" or content == "doctype html" or content == "DOCTYPE HTML" or content == "DOCTYPE html":
        return "HTML-5.0"
    elif content.find("html4")!=-1 or content.find("HTML4")!= -1 or content.find("HTML 4.01")!=-1 or content.find("html 4.01"):
        return "HTML-4.01"
    elif content.find("html3")!=-1 or content.find("HTML3")!= -1 or content.find("HTML 3.2")!=-1 or content.find("html 3.2"):
        return "HTML-3.2"
    elif content.find("html2")!=-1 or content.find("HTML2")!= -1 or content.find("HTML 2.0")!=-1 or content.find("html 2.0"):
        return "HTML-2.0"
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
    forms = soup.findAll('input', type='password')

    if len(forms) > 0:
        return True
    else:
        return False

def get_links_info(url, soup):
    base_parts = urlparse(url)
    links_info = [0, 0, 0]
    for a in soup.find_all('a'):
        link_parts = urlparse(a.get('href'))
        #check internal link
        if base_parts.scheme == link_parts.scheme and base_parts.netloc == link_parts.netloc:
            links_info[0] = links_info[0]+1
        #check external link
        else:
            links_info[1] = links_info[1]+1
        #check inaccesible link
        if checkInaccessible(url):
            links_info[2] = links_info[2]+1
    return links_info


def checkInaccessible(url):
    try:
        validate = URLValidator()
        validate(url)
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = urlopen(url, context=ctx)
        except HTTPError as e:
            return True 
        except URLError as e:
            return True 
    except ValidationError:
        return True
    return False 


def getInfo(url):

    try:
        validate = URLValidator()
        validate(url)
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = urlopen(url, context=ctx)
        except HTTPError as e:
            result = Webpage()
            result.address = url
            result.errorType = 1
            result.statusCode = e.code
            result.errorMessage = e
            return result 
        except URLError as e:
            result = Webpage()
            result.address = url
            result.errorType = 2
            result.errorMessage = e.args[0]
            return result 
        soup = BeautifulSoup(response, "html.parser")

        #html version of the page
        html_version = get_html_version(soup.contents[0])

        #page title
        page_title = soup.title.string

        # status code 
        status_code = response.getcode()

        # time_stamp
        time_stamp = ""

        headings = get_heading_info(soup)

        login_forms = get_forms_info(soup)

        link_counts = get_links_info(url, soup)

        result = Webpage()
        result.address = url
        result.statusCode = status_code
        result.version = html_version
        result.title = page_title
        result.timeStamp = time_stamp
        result.internalLinkCount = link_counts[0]
        result.externalLinkCount = link_counts[1]
        result.inaccessibleLinkCount = link_counts[2]
        result.loginForm = login_forms
        result.h1Count = headings['h1']
        result.h2Count = headings['h2']
        result.h3Count = headings['h3']
        result.h4Count = headings['h4']
        result.h5Count = headings['h5']
        result.h6Count = headings['h6']
        result.errorType = 0
        result.errorMessage = "Success"
        print(result)
        return result

    except ValidationError:
        result = Webpage()
        result.errorType = 3
        result.errorMessage = "URL not valid."
        return result 
