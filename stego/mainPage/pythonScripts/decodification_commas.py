import os
import re


#If len > 0, the HTML line given contains single and/or double quotation marks
def quotation_marks_lines (input):
    re_list = [r'"(.*?)"', r"'(.*?)'"]
    matches = []

    for r in re_list:
        matches += re.findall(r, input)

    return len(matches)



def total_capacity (input):
    maxbits = 0
    for line in input.splitlines():
        maxbits += quotation_marks_lines(line)

    return maxbits



#Takes the HTML lines with quotation marks and returns the codification
#depending on if it has single or double quotation marks.
def retrieve_msg_commas (input):
    relist = r'"(.*?)"'
    relist2 = r"'(.*?)'"
    double = {}

    if (quotation_marks_lines (input) > 0):
        p = re.compile(relist)
        for m in p.finditer(input):
            double[m.start()] = 1

        p = re.compile(relist2)
        for m in p.finditer(input):
            double[m.start()] = 0

        sdouble = sorted(double.items())

        bits = [value[1] for value in sdouble]

        for bit in bits:
            msg.append(bit)



def main():

    with open(os.getcwd()+"/stego/tempResponseAlejandroCommas.html") as fd:
        content = fd.read()

    hlines = content.splitlines()

    msg = []
    for line in hlines:
        tmp = retrieve_msg_commas(line)
        if(tmp is not None):
            msg.append()

            print(msg)


if __name__ == "__main__":
    # test_bits_total()
    # test_num_attributes_line()
    main()
