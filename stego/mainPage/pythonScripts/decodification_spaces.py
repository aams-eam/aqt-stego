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
    re_1 = r'<'
    re_2 = r'>'
    double = {}
    msg = []

    if(tag_lines(input) > 0):
        p = re.compile(re_1)
        for match in p.finditer(input):
            if(input[match.end()] == " "):
                double[match.end()-1] = "1"
            else:
                double[match.end()-1] = "0"

        p = re.compile(re_2)
        for match in p.finditer(input):
            if(input[match.start() - 1] == " "):
                double[match.start()] = "1"
            else:
                double[match.start()] = "0"

        sdouble = sorted(double.items())

        bits = [value[1] for value in sdouble]

        for bit in bits:
            msg.append(bit)

    return msg

def main():

    # with open(os.getcwd()+"/stego/tempResponseContent.html") as fd:
    with open(os.getcwd()+"/stego/ResponseContent.html") as fd:
        content = fd.read()

    hlines = content.splitlines()

    msg = []
    for line in hlines:
        tmp = retrieve_msg_spaces(line)
        if(tmp is not None):
            msg += tmp

            print(msg)

if __name__ == "__main__":
    # test_bits_total()
    # test_num_attributes_line()
    main()
