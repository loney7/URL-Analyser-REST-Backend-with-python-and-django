from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import Form
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
                resultObjInitial = cache.get(address)
                print('cache found')
            else:
                resultObjInitial = scrapingHelper.getInfo(address)
            # #   resultString = str(resultObjInitial)
            #     res = {}
            #     res['address'] = "0"
            #     res['errorMessage'] = "0"
            #     res['title'] = e
            #     res['internalLinkCount'] = "0"
            #     res['externalLinkCount'] = "0"
            #     res['inaccessibleLinkCount'] = "0"
            #     res['h1Count'] = "0"
            #     res['h2Count'] = "0"
            #     res['h3Count'] = "0"
            #     res['h4Count'] = "0"
            #     res['h5Count'] = "0"
            #     res['h6Count'] = "0"
            #     res['version'] = "0"
            #     res['timeStamp'] = "0"
            #     res['loginForm'] = "0"
            #     res['errorType'] = "0"
            #     res['statusCode'] = "0"


                print(resultObjInitial.address)
                print(resultObjInitial.errorMessage)
                print(resultObjInitial.title)
                print(resultObjInitial.externalLinkCount)
                print(resultObjInitial.errorType)
                print(resultObjInitial.h1Count)
                print(resultObjInitial.h2Count)
                print(resultObjInitial.h3Count)
                print(resultObjInitial.h4Count)
                print(resultObjInitial.h5Count)
                print(resultObjInitial.h6Count)
                print(resultObjInitial.version)
                print(resultObjInitial.inaccessibleLinkCount)
                print(resultObjInitial.internalLinkCount)
                print(resultObjInitial.statusCode)



                cache.set(address, resultObjInitial, 60)
            #
            # resultObj = Webpage()
            # resultStringAttr = resultString.split("~")
            # print(resultStringAttr)
            # resultObj.address = resultStringAttr[0]
            # resultObj.errorType = int(resultStringAttr[1])
            # resultObj.h1Count = int(resultStringAttr[2])
            # resultObj.h2Count = int(resultStringAttr[3])
            # resultObj.h3Count = int(resultStringAttr[4])
            # resultObj.h4Count = int(resultStringAttr[5])
            # resultObj.h5Count = int(resultStringAttr[6])
            # resultObj.h6Count = int(resultStringAttr[7])
            # resultObj.version = resultStringAttr[8]
            # resultObj.internalLinkCount = int(resultStringAttr[9])
            # resultObj.externalLinkCount = int(resultStringAttr[10])
            # resultObj.inaccessibleLinkCount = int(resultStringAttr[11])
            # resultObj.statusCode = int(resultStringAttr[12])
            # resultObj.timeStamp = resultStringAttr[13]
            # resultObj.loginForm = bool(resultStringAttr[14])
            # resultObj.errorMessage = resultStringAttr[15]

            context = {
                "webpage":resultObjInitial
            }
            if resultObjInitial.errorType == 0:
                return render(request, 'result.html', context)
            elif resultObjInitial.errorType == 1:
                return render(request, 'resultHTTPError.html', context)
            elif resultObjInitial.errorType == 2:
                return render(request, 'resultURLError.html', context)
            else:
                return render(request, 'resultInvalidURL.html', context)
    else:
        form = Form()
    context = {
        "form":form
    }
    return render(request, "form.html", context)
