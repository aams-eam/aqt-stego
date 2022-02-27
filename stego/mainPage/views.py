### DJANGO IMPORTS ###
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt

### NATIVE IMPORTS ###
import os
from random import choice

### CIPHERING IMPORTS ###
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
K1 = "ca729843da49dc89e95e57f8cb78ea2e45b58594" # Pre-shared key between client2 and the webserver


### FUNCTIONS ###
def writetofile(content, filedir):
    f = open(os.getcwd()+'/'+filedir, 'w')
    testfile = File(f)
    testfile.write(content)
    testfile.close
    f.close
    return HttpResponse()



def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')



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

        if(rpass is not None):
            # buscar un archivo con nombre pass.html
            # si no existe devolver lo otro, si existe devolverlo

            try: # if the file exists do the encode and encryption -->

                # GET THE MSG
                with open(rpass+".html", 'r') as fd:
                    msg = fd.read()


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


                # CREATE LIST OF BITS WITH THE MESSAGE
                mbits = msg2lbits(msg) # list of bits with the message
                mlength_bytes = bitstring_to_bytes("{0:b}".format(len(mbits)).zfill(basebits_of_len))

                # GENERATE RANDOM SESSION KEY OF 160 BITS
                random = get_random_bytes(16)
                K2 = SHA.new(random).digest() # 160 bits key length

                # CIPHER THE MESSAGE WITH THE K2 AND K1 USING RC4 ALGORITHM
                cipher = ARC4.new(K2)
                encmsg = cipher.encrypt(msg.encode('utf-8')) # Encrypt the message with K2
                cipher = ARC4.new(bytes.fromhex(K1))
                encmsg = cipher.encrypt(encmsg) # Encrypt the message with K1
                K2length = K2 + mlength_bytes
                encK2length = cipher.encrypt(K2length) # Encrypt the key with the length concatenated

                init = ['1', '0', '0', '1', '1', '0', '0', '0'] # Indicator of start of message
                encmsg_bits = bits2lbits(encmsg) # encoded msg to list of bits
                encK2length_bits = bits2lbits(encK2length) # encoded K2 concatenated with length


                # K2 and length encrypted with K1 and concatenated with random bits until the end
                payloadatt = encK2length_bits + [choice(['1', '0']) for i in range(maxbits_att-len(encK2length_bits))]

                # init and msg encrypted with K1 repeated and padded with random bits
                payloadmsg_quotes = init + encmsg_bits
                payloadmsg_quotes = payloadmsg_quotes*(int(maxbits_quote/len(payloadmsg_quotes)))
                payloadmsg_quotes = payloadmsg_quotes + [choice(['1', '0']) for i in range(maxbits_quote-len(payloadmsg_quotes))]

                # init and msg encrypted with K1 repeated and padded with random bits
                payloadmsg_spaces = init + encmsg_bits
                payloadmsg_spaces = payloadmsg_spaces*(int(maxbits_tag/len(payloadmsg_spaces)))
                payloadmsg_spaces = payloadmsg_spaces + [choice(['1', '0']) for i in range(maxbits_tag-len(payloadmsg_spaces))]

                # MODIFY THE HTML
                newhtml = []

                # ENCODE payloadatt IN ATTRIBUTES
                for line in actualhtml.splitlines():

                    newline = att_encode_line(line, payloadatt)
                    newhtml.append(newline)

                # TEMP*** Uncomment when Ivan Torrejon finish his functions
                # # ENCODE payloadmsg multiple times with tag codification
                # newhtml2 = []
                # for line in newhtml:
                #
                #     newline = spaces_encode_line(line, payloadmsg_quotes)
                #     newhtml2.append(newline)
                #
                # # ENCODE pyaload msg multiple times with quotes codification
                # newhtml3 = []
                # for line in newhtml:
                #
                #     newline = commas_encode_line(line, payloadmsg_spaces)
                #     newhtml3.append(newline)


                # Store the new html in file with name of the pass
                modifiedhtml = "\n".join(newhtml) # TEMP***
                # modifiedhtml = "\n".join(newhtml3)

                print(modifiedhtml)

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
        if(((INIT_LEN + msg_len) >  maxbits_quote) and ((INIT_LEN + msg_len) >  maxbits_tag)):
            # return 404 not found as indicator
            return HttpResponseNotFound("404 NOT FOUND")


        # Write parameters in `rpass`.html file
        with open(rpass+".html", 'w') as fd:
            fd.write(msg)


        return render(request, 'mainPage/indexExpanded.html')
