from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
import os
from .attPosition import encode_line
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
        if((rpass is not None) and (tpass is not None)):
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
        if((rpass is None) or (msg is None or '')):
            return render(request, 'mainPage/indexExpanded.html')
        else:
            tpass = rpass


        # GET BASE HTML
        htmlresponse = render(request, 'mainPage/indexExpanded.html')
        actualhtml = htmlresponse.content.decode("utf-8")


        # GETTING MAC CAPACITY AND
        # See if the message fits in the capacity of the html
        maxbits = total_capacity(actualhtml) # Total capacity
        # TEMP*** In this case the bits used for
        # describing the length are the ones necessary for the full capacity length
        basebits_of_len = len("{0:b}".format(maxbits))
        # TEMP***


        # CONFIGURATION PARAMETERS
        try:
            bits_of_len = int(request.POST.get('bitlen', basebits_of_len))
        except ValueError:
            bits_of_len = basebits_of_len

        try:
            bits_of_key = int(request.POST.get('keylen', 16))
        except ValueError:
            bits_of_key = 16

        try:
            redundancy = int(request.POST.get('redundancy', 1))
        except ValueError:
            redundancy = 1



        if((len(msg)*8 + bits_of_len + bits_of_key)*redundancy >  maxbits):
            return render(request, 'mainPage/indexExpanded.html')




        # MODIFY THE HTML
        newhtml = []
        # convert message in list of bytes
        byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(msg, "utf8")]
        # conver list of bytes in list of bits
        mbits = [bit for byte in byte_list for bit in byte]

        # HOW TO SEPARATE THE MESSAGE TO ENCODE IT
        # PUT IT AS MANY TYPES WITH CERTAIN SEPARATION OR WHAT?
        mlength = list("{0:b}".format(len(mbits)).zfill(bits_of_len))
        print(mlength)
        key = [] # TEMP *** KEY FOR CIPHERING # known length for the receiver # MAYBE CIPHER ONLY THE KEY WITH PUBLIC CRYPTOGRAPHY
        encriptedm = mbits # TEMP *** CIPHER THE MESSAGE
        init = [] # TEMP*** initial message that identifies the start of a message
        # FINAL PAYLOAD
        payload = init + mlength + key + mbits

        print(payload)


        # ENCODING
        print("ENCODING")
        for line in actualhtml.splitlines():

            newline = encode_line(line, payload)
            newhtml.append(newline)
        # MODIFY THE HTML

        # Store the new html in temporary variable modifiedhtml
        modifiedhtml = "\n".join(newhtml)

        return render(request, 'mainPage/indexExpanded.html')
