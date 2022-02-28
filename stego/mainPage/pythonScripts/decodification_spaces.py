import os
import re

#If len > 0, the HTML line given contains this kind of brackets < >
def tag_lines (input):
    re_list = ['<', '>']
    matches = []

    for r in re_list:
        matches += re.findall(r, input)

    return len(matches)


def total_capacity (input):
    maxbits = 0
    for line in input.splitlines():
        maxbits += tag_lines(line)

    return maxbits



#Takes the HTML lines with HTML tags and returns the codification
#depending on if it has a space between the brackets or not.
def retrieve_msg_spaces (input):
    match1 = re.search('<\s', input)
    match2 = re.search('\s>', input)
    msg = []

    if(tag_lines(input) > 0):
        if (match1):
            msg.append("1")
        else:
            msg.append("0")


        if (match2):
            msg.append("1")
        else:
            msg.append("0")

    return msg

def main():

    with open(os.getcwd()+"/stego/tempResponseAlejandroSpaces.html") as fd:
        content = fd.read()

    hlines = content.splitlines()

    msg = []
    for line in hlines:
        tmp = retrieve_msg_spaces(line)
        if(tmp is not None):
            msg.append()

            print(msg)

if __name__ == "__main__":
    # test_bits_total()
    # test_num_attributes_line()
    main()
