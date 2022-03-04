import os
import re
from pprint import pprint
from bs4 import BeautifulSoup


def get_attributes(content):

    fatt = None

    # --- OBTAIN AL EXISTENT ATTRIBUTES --->
    if(content.find("< ") >= 0):
        content = content.replace("< ", "<")

    if(content.find(" >") >= 0):
        content = content.replace(" >", ">")

    soup = BeautifulSoup(content, 'html.parser')
    # [tag.attrs for tag in soup.findAll('a')]
    try:
        fatt = soup.find_all()[0].attrs
        if(len(fatt)==0):
            fatt = None

    except IndexError as e:
        fatt = None
    # <--- OBTAIN AL EXISTENT ATTRIBUTES ---

    return fatt



def get_clean_tag(line):

    isclean = False
    tag = None

    pattern = r'<(.*?)>'
    match = re.search(pattern, line)

    # See that there is a tag in the line
    if(match):
        # discard all spaces but the ones inside the tag
        tag = match.group()

        # See that is not a comment
        if((tag.find("<!--")==-1) and (tag.find("< !--")==-1)):
            isclean = True

    return isclean, tag



def num_attributes_line(line):

    maxlines = 0

    isclean, content = get_clean_tag(line)

    if(isclean):

        att = get_attributes(content)
        if(att is not None):
            maxlines = len(att)

    return maxlines



def num_att2bits(num_att):

    num_bits = 0

    # TEMP*** apply log base 2 to (line!)
    # TEMP*** then create new algorithm in encode_line() func
    if(num_att > 1):
        num_bits = num_att-1

    return num_bits



def max_bits_line(line):

    num_att = num_attributes_line(line)

    return num_att2bits(num_att)



def total_capacity(html):

    maxbits = 0

    for line in html.splitlines():
        maxbits += max_bits_line(line)

    return maxbits



def encode_line(line, mbits):

    maxlines = 0
    enc = None

    isclean, content = get_clean_tag(line)

    if(isclean):

        attd = get_attributes(content) # attributes in a dict
        # if there is a list in values join it with space

        if(attd is not None):
            att = {}
            for entry in attd.items():
                if(type(entry[1])==list):
                    att[entry[0]] = " ".join(entry[1])
                else:
                    att[entry[0]] = entry[1]


            # get number of bits that can be encoded
            if(att is not None):
                num_bits = num_att2bits(len(att))
        else:
            num_bits = 0


        if((num_bits > 0) and (len(mbits) > 0)):

            # get part of the message
            mbits_part = mbits[:num_bits]
            del mbits[:num_bits]


            # ORDER DICTIONARY TAKING INTO ACCOUNT THE PROPOSED ALGORITHM
            def sort_att_trasnformation(d):

                # sorted value
                sv = []
                sv[:] = d # separate into list of characters
                sv.sort() # sort alphabetically
                sv.append(sv[0]) # put first char at the end
                del sv[0] # delete first char so second char is the first
                sv = ''.join(sv) # recreate string from the list
                return sv

            # This is the dictionary base to encode
            att_sorted = sorted(att.items(),
                            key = lambda x: sort_att_trasnformation(x[0]), reverse=True)


            # apply algorithm to encode bits
            i = 0
            for m in mbits_part:

                if(m=="0"):
                    att_sorted[i+1], att_sorted[i] = att_sorted[i], att_sorted[i+1]
                i += 1

            # create a new line with the sorted attributes
            # the complexity is added if it is tried to mantain the spaces
            # and the quotes if "" or ''
            keylist = list(att.keys())
            firstpart = line[0:line.find(keylist[0])]
            pos = line.find(" >")
            if(pos>=0):
                secondpart=line[pos:]
            else:
                pos = line.find(">")
                secondpart = line[pos:]

            attpart = []
            for a in att_sorted:

                if(not a[1]==''):

                    if(line[line.find(a[0])+len(a[0])+1]=="\""): # to mantain original quotes
                        attpart.append(a[0]+"=\""+a[1]+"\"")
                    else:
                        attpart.append(a[0]+"='"+a[1]+"'")

                else:
                    attpart.append(a[0])


            attpart = " ".join(attpart)
            return firstpart+attpart+secondpart

    return line



def decode_line(line):

    bits = None

    isclean, content = get_clean_tag(line)

    if(isclean):

        att = get_attributes(content) # attributes in a dict

        if(not att==None):


            # ORDER DICTIONARY TAKING INTO ACCOUNT THE PROPOSED ALGORITHM
            def sort_att_trasnformation(d):

                # sorted value
                sv = []
                sv[:] = d # separate into list of characters
                sv.sort() # sort alphabetically
                sv.append(sv[0]) # put first char at the end
                del sv[0] # delete first char so second char is the first
                sv = ''.join(sv) # recreate string from the list
                return sv

            # This is the dictionary base to encode
            keys_sorted = sorted(att.keys(),
                            key = lambda x: sort_att_trasnformation(x), reverse=True)[::-1]


            # compare att_sorted with att
            attkeys = list(att.keys())[::-1]
            bits = []
            for i in range(len(attkeys)-1):
                if(attkeys[i]==keys_sorted[i]):
                    bits.append("1")
                else:
                    bits.append("0")
                    attkeys[i], attkeys[i+1] = attkeys[i+1], attkeys[i]

            bits = bits[::-1]

    return bits



test = [
    "          <link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\">       ", # 2
    "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\" >    ",
    "     < link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\">",
    "           <link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\" >     ",
    "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\">",
    "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\">",
    "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" >",
    "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" >",
    "<link>",
    "< link>",
    "<link >",
    "< link >",
    "<!-- ======= Slider Section ======= -->",
    "<!-- ======= Slider Section ======= -- >",
    "< !-- ======= Slider Section ======= -->",
    "< !-- ======= Slider Section ======= -- >",
    '<iframe src="http://longurl" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen>',
    '< iframe src="http://longurl" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen>',
    '<iframe src="http://longurl" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen >',
    '< iframe src="http://longurl" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen >',
    '<!DOCTYPE html>',
    '< !DOCTYPE html>',
    '<!DOCTYPE html >',
    '< !DOCTYPE html >',
    '<meta content="width=device-width, initial-scale=1.0" name="viewport">',
    '< meta content="width=device-width, initial-scale=1.0" name="viewport">',
    '<meta content="width=device-width, initial-scale=1.0" name="viewport" >',
    '< meta content="width=device-width, initial-scale=1.0" name="viewport" >',
]

output = [
    2,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    6,
    6,
    6,
    6,
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    2,
]



def main():

    newhtml = []
    # take first num_bits from the message
    message = "Mensaje a codificar"
    # convert message in list of bytes
    byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(message, "utf8")]
    # conver list of bytes in list of bits
    mbits = [bit for byte in byte_list for bit in byte]
    probe = mbits.copy() # To compare the result after Encoding and Decoding

    # ENCODING
    print("ENCODING")
    print("objective:\t" + str(mbits))
    for t,o in zip(test, output):

        newline = encode_line(t, mbits)
        newhtml.append(newline)

    htmlString = "\n".join(newhtml)


    # DECODING
    print("DECODING")
    totalbits = []
    for line in newhtml:
        bits_part = decode_line(line)
        if(not bits_part==None):
            totalbits = totalbits + bits_part


    # ASSERTION
    mincapacity = len(probe)
    if(len(totalbits) < mincapacity):
        mincapacity = len(totalbits)
    print("result:\t\t" +str(totalbits[:mincapacity]))
    assert(probe[:mincapacity]==totalbits[:mincapacity])




# test to get all the possible bits to embed in a html file
def test_bits_total():

    print("Working directory:", os.getcwd())
    with open(os.getcwd()+"/stego/responseContent.html") as fd:
        content = fd.read()

    # content = '<input type="text" data-msg="Please enter at least 8 chars of subject" />' # 2

    hlines = content.splitlines()
    print("\n")
    print("Total HTML characters:\t", len(content))
    print("Total HTML lines:\t", len(hlines))

    bits = 0

    for line in hlines:
        bits += max_bits_line(line)

    print("Total Bits to embed:\t", bits, "\n")





# test if num_attributes_line works properly
def test_num_attributes_line():

        for t,o in zip(test, output):

            num_att = num_attributes_line(t)
            print(t, o, num_att)
            assert(o==num_att)



if __name__ == "__main__":
    # test_bits_total()
    # test_num_attributes_line()
    main()
