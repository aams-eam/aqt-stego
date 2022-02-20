from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
import os


# FUNCTIONS
def writetofile(content, filedir):
    f = open(os.getcwd()+'/'+filedir, 'w')
    testfile = File(f)
    testfile.write(content)
    testfile.close
    f.close
    return HttpResponse()


# Create your views here.
def home(request):

    # CODE INDEX MANIPULATION


    response =  render(request, 'mainPage/indexExpanded.html')

    print()
    print()
    print()
    print("comment  ")
    print()
    print()
    print()

    # writetofile(response.content.decode(response.charset), "responseContent.html")

    # with open("responseContent.html", 'w') as fd:
    #     fd.write(response.content.decode(response.charset))

    return response
