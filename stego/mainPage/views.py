### DJANGO IMPORTS ###
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt

### NATIVE IMPORTS ###
import os

### ENCODING SCRIPTS IMPORTS ###
from .attPosition import encode_line as att_encode_line
from .attPosition import total_capacity as att_total_capacity
from .attPosition import max_bits_line as att_max_bits_line

### CIPHERING IMPORTS ###
import sslcrypto
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes


### FUNCTIONS ###
def writetofile(content, filedir):
    f = open(os.getcwd()+'/'+filedir, 'w')
    testfile = File(f)
    testfile.write(content)
    testfile.close
    f.close
    return HttpResponse()



def key2lbits(key):
    # convert message in list of bytes
    byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(key)]
    # conver list of bytes in list of bits
    kbits = [bit for byte in byte_list for bit in byte]
    return kbits



def msg2lbits(msg):
    # convert message in list of bytes
    byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(msg, "utf8")]
    # conver list of bytes in list of bits
    mbits = [bit for byte in byte_list for bit in byte]
    return mbits



# Create your views here.
def home(request):

    return render(request, 'mainPage/indexExpanded.html')



### VIEWS ###
@csrf_exempt
def falseShop(request):

    # CODE INDEX MANIPULATION
    if request.method == 'GET':

        # see if it exists parameter pass and compare with tpass
        rpass = request.GET.get('pass', None)
        if(rpass is not None):
            # buscar un archivo con nombre pass.html
            # si no existe devolver lo otro, si existe devolverlo

            try:
                with open(rpass+".html", 'r') as fd:
                    modifiedhtml = fd.read()
                    print(modifiedhtml)

                    # Return modified page
                    htmlresponse = render(request, 'mainPage/indexExpanded.html')
                    htmlresponse.content = modifiedhtml

                    # TEMP*** remove the file
                    return htmlresponse

            except FileNotFoundError:
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
        maxbits = att_total_capacity(actualhtml) # Total capacity
        print("MAXBITS:", maxbits)
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
        mbits = msg2lbits(msg) # list of bits with the message
        mlength = list("{0:b}".format(len(mbits)).zfill(bits_of_len)) # length of the message

        # GENERATE SESSION KEY OF 160 BITS
        random = get_random_bytes(16)
        session_key = SHA.new(random).digest() # 160 bits key length
        kbits = key2lbits(session_key)

        # CIPHER THE MESSAGE WITH THE SESSION KEY AND ARC4
        cipher = ARC4.new(session_key)
        encmsg = cipher.encrypt(msg)
        print("MSG:", len(msg), msg)
        print("CIPHERMESSAGE:", len(encmsg), encmsg)

        init = ['1', '0', '0', '1', '1', '0', '0', '0'] # Indicator of start of message
        # FINAL PAYLOAD
        payload = init + mlength + kbits + mbits

        print(payload)


        # ENCODING
        print("ENCODING")
        for line in actualhtml.splitlines():

            newline = att_encode_line(line, payload)
            newhtml.append(newline)
        # MODIFY THE HTML

        # Store the new html in file with name of the pass
        modifiedhtml = "\n".join(newhtml)

        with open(rpass+".html", 'w') as fd:
            fd.write(modifiedhtml)

        return render(request, 'mainPage/indexExpanded.html')
