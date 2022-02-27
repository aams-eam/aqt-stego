### DJANGO IMPORTS ###
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt

### NATIVE IMPORTS ###
import os

### CIPHERING IMPORTS ###
import sslcrypto
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes

### ENCODING SCRIPTS IMPORTS ###
from .pythonScripts.attPosition import encode_line as att_encode_line
from .pythonScripts.attPosition import total_capacity as att_total_capacity
from .pythonScripts.attPosition import max_bits_line as att_max_bits_line
from .pythonScripts.decodification_commas import total_capacity as quot_total_capacity
from .pythonScripts.decodification_spaces import total_capacity as space_total_capacity




### GLOBAL VARIABLES ###
SESSIONKEY_LEN = 160 # Number of bits of the session key
INIT_LEN = 8         # Number of bits in the init string


### FUNCTIONS ###
def writetofile(content, filedir):
    f = open(os.getcwd()+'/'+filedir, 'w')
    testfile = File(f)
    testfile.write(content)
    testfile.close
    f.close
    return HttpResponse()



def bits2lbits(key):
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

        # see if it exists parameter pass
        rpass = request.GET.get('pass', None)
        pubkey = request.GET.get('pubkey', None)

        if((rpass is not None) and (pubkey is not None)):
            # buscar un archivo con nombre pass.html
            # si no existe devolver lo otro, si existe devolverlo

            try: # if the file exists do the encode and encryption -->
                with open(rpass+".html", 'r') as fd:


                    # GET BASE HTML
                    htmlresponse = render(request, 'mainPage/indexExpanded.html')
                    actualhtml = htmlresponse.content.decode("utf-8")

                    # MAX BITS OF EACH ENCODING
                    maxbits_att = att_total_capacity(actualhtml) # Total capacity
                    maxbits_quote = quot_total_capacity(actualhtml) # capacity of space encoding
                    maxbits_tag = space_total_capacity(actualhtml) # capacity of quotes encoding
                    # TEMP*** In this case the bits used for
                    # describing the length are the ones necessary for the max capacity of
                    # quote or spaces
                    basebits_of_len = len("{0:b}".format(max(maxbits_quote, maxbits_tag)))

                    # GET THE MSG
                    with open(rpass+".html", 'r') as fd:
                        msg = fd.read()


                    # CREATE LIST OF BITS WITH THE MESSAGE
                    mbits = msg2lbits(msg) # list of bits with the message
                    mlength = list("{0:b}".format(len(mbits)).zfill(basebits_of_len)) # length of the message

                    # GENERATE SESSION KEY OF 160 BITS
                    random = get_random_bytes(16)
                    session_key = SHA.new(random).digest() # 160 bits key length

                    # LOAD PUBLIC KEY
                    pubkeyb = bytes.fromhex(pubkey)

                    # CIPHER SIMMETRIC KEY WITH PUBLIC KEY
                    curve = sslcrypto.ecc.get_curve("secp192k1")
                    enckey = curve.encrypt(session_key, pubkeyb, algo="aes-256-ofb")

                    # CIPHER THE MESSAGE WITH THE SESSION KEY AND ARC4
                    cipher = ARC4.new(session_key)
                    encmsg = cipher.encrypt(msg.encode('utf-8'))

                    init = ['1', '0', '0', '1', '1', '0', '0', '0'] # Indicator of start of message
                    encmsgbits = bits2lbits(encmsg) # encoded msg to list of bits
                    enckeybits = bits2lbits(enckey) # encoded key to list of bits


                    payloadatt = enckeybits + mlength # TEMP*** concat random bits until the end
                    payloadmsg = init + encmsgbits # TEMP*** make robustness and concatenate random bits if space left

                    # MODIFY THE HTML
                    newhtml = []

                    # ENCODE payloadatt IN ATTRIBUTES
                    for line in actualhtml.splitlines():

                        newline = att_encode_line(line, payloadatt)
                        newhtml.append(newline)

                    # ENCODE payloadmsg multiple times with tag codification
                    newhtml2 = []
                    for line in newhtml:

                        newline = spaces_encode_line(line, payloadmsg)
                        newhtml2.append(newline)

                    # ENCODE pyaload msg multiple times with quotes codification
                    newhtml3 = []
                    for line in newhtml:

                        newline = commas_encode_line(line, payloadmsg)
                        newhtml3.append(newline)


                    # Store the new html in file with name of the pass
                    modifiedhtml = "\n".join(newhtml)
                    # modifiedhtml = "\n".join(newhtml3)

                    # Return modified page
                    htmlresponse = render(request, 'mainPage/indexExpanded.html')
                    htmlresponse.content = modifiedhtml

                    # TEMP*** remove the file
                    return htmlresponse

            except FileNotFoundError:
                return render(request, 'mainPage/indexExpanded.html')

        return render(request, 'mainPage/indexExpanded.html')

    else:

        # Store the password and message
        rpass = request.POST.get('pass', None)
        msg = request.POST.get('msg', None)

        # see if pass and msg are not None
        if((rpass is None) or (msg is None or '')):
            return render(request, 'mainPage/indexExpanded.html')


        # GET BASE HTML
        htmlresponse = render(request, 'mainPage/indexExpanded.html')
        actualhtml = htmlresponse.content.decode("utf-8")

        # MAX BITS OF EACH ENCODING
        maxbits_att = att_total_capacity(actualhtml) # Total capacity
        maxbits_quote = quot_total_capacity(actualhtml) # capacity of space encoding
        maxbits_tag = space_total_capacity(actualhtml) # capacity of quotes encoding

        print(maxbits_att,maxbits_quote,maxbits_tag)

        # TEMP*** In this case the bits used for
        # describing the length are the ones necessary for the max capacity of
        # quote or spaces
        basebits_of_len = len("{0:b}".format(max(maxbits_quote, maxbits_tag)))
        msg_len = len(msg2lbits(msg))

        # sufficient capacity for key and length descriptor in att
        if((SESSIONKEY_LEN + basebits_of_len) >  maxbits_att):
            # return 404 not found as indicator
            return HttpResponseNotFound("404 NOT FOUND")

        # sufficient capacity for init and message in quotes and spaces encoding
        if((INIT_LEN + msg_len) >  maxbits_att):
            # return 404 not found as indicator
            return HttpResponseNotFound("404 NOT FOUND")


        # Write parameters in `rpass`.html file
        with open(rpass+".html", 'w') as fd:
            fd.write(msg)


        return render(request, 'mainPage/indexExpanded.html')
