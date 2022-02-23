from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
import os
from .attPosition import total_capacity


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

    return render(request, 'mainPage/indexExpanded.html')


# temporal password, in an ideal way, this will be a database
# of hashed passwords and modified htmls
# mutex should be used here
tpass = None
modifiedhtml = None


@csrf_exempt
def falseShop(request):

    # CODE INDEX MANIPULATION
    if request.method == 'GET':

        # see if it exists parameter pass and compare with tpass
        rpass = request.GET.get('pass', None)
        if(rpass is not None):
            if(tpass==rpass): # message has been stored with that password
                # Return modified page
                htmlresponse = render(request, 'mainPage/indexExpanded.html')
                htmlresponse.content = modifiedhtml
                return htmlresponse

        return render(request, 'mainPage/indexExpanded.html')

    else:

        # Store the password and message
        rpass = request.POST.get('pass', None)
        msg = request.POST.get('msg', None)

        # see if pass and msg are not None
        if((rpass is not None) and (msg is not None or '')):
            tpass = rpass

            # get base html
            htmlresponse = render(request, 'mainPage/indexExpanded.html')
            actualhtml = htmlresponse.content.decode("utf-8")


            # MODIFY THE HTML
            newhtml = []
            # convert message in list of bytes
            byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(msg, "utf8")]
            # conver list of bytes in list of bits
            mbits = [bit for byte in byte_list for bit in byte]


            # Cipher the message

            # How to separate the message to encode it
            maxbits = total_capacity(actualhtml) # Total capacity
            # see that total capacity is higher than len of the message
            # two bytes of length and two x bytes for random key
            if(len(mbits) + 16 <  maxbits):

                # ENCODING
                print("ENCODING")
                for line in actualhtml.splitlines():

                    newline = encode_line(line, mbits)
                    newhtml.append(newline)
                # MODIFY THE HTML

                # Store the new html in temporary variable modifiedhtml
                modifiedhtml = "\n".join(newhtml)


        return render(request, 'mainPage/indexExpanded.html')


    # writetofile(response.content.decode(response.charset), "responseContent.html")

    # with open("responseContent.html", 'w') as fd:
    #     fd.write(response.content.decode(response.charset))

    return response
