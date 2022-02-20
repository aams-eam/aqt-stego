import os
import re
from pprint import pprint



def num_attributes_line(line):

    maxlines = 0

    pattern = r'<(.*?)>'
    match = re.search(pattern, line)

    # See that there is a tag in the line
    if(match):
        # discard all spaces but the ones inside the tag
        content = match.group()

        # See that is not a comment
        if((content.find("<!--")==-1) and (content.find("< !--")==-1)):

            words = content.split(" ") # TEMP*** with this you are also separating spaces between values

            # --- OBTAIN AL EXISTENT ATTRIBUTES --->
            # if there is out of index error it would be a single tag:
            # <link>
            # < link>
            # <link >
            # < link >
            try:
                ## delete the tag and "<"
                if (words[0]=='<'):
                    del words[0:2]
                elif (words[0].find('<')>=0):
                    del words[0]

                ## delete the end ">"
                if (words[-1]=='>'):
                    del words[-1]
                elif(words[0].find('>')):
                    # delete only the '>' to get the complete attribute
                    temp = words[-1][0:len(words[-1])-1]
                    del words[-1]
                    words.append(temp)

                maxlines =  len(words)

            except IndexError as e:
                maxlines = 0
            # <--- OBTAIN AL EXISTENT ATTRIBUTES ---

    return maxlines



def max_bits_line(line):

    num_bits = 0
    num_att = num_attributes_line(line)

    if(num_att > 1):
        num_bits = num_att-1

    return num_bits



def main():

    # test = [
    #     "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\">", # 2
    #     "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\" >",
    #     "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\">",
    #     "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\" >",
    #     "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\">",
    #     "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\">",
    #     "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" >",
    #     "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" >",
    #     "<link>",
    #     "< link>",
    #     "<link >",
    #     "< link >",
    #     "<!-- ======= Slider Section ======= -->",
    #     "<!-- ======= Slider Section ======= -- >",
    #     "< !-- ======= Slider Section ======= -->",
    #     "< !-- ======= Slider Section ======= -- >",
    # ]
    #
    # output = [
    #     2,
    #     2,
    #     2,
    #     2,
    #     1,
    #     1,
    #     1,
    #     1,
    #     0,
    #     0,
    #     0,
    #     0,
    #     0,
    #     0,
    #     0,
    #     0,
    # ]

    print("Working directory:", os.getcwd())
    with open(os.getcwd()+"/stego/responseContent.html") as fd:
        content = fd.read()

    content = '<input type="text" data-msg="Please enter at least 8 chars of subject" />' # 2

    hlines = content.splitlines()
    print("Total HTML lines:", len(hlines))

    tdict = {}
    cont = 0

    for line in hlines:

        num_att = num_attributes_line(line)
        # print(num_att)
        tdict[cont] = num_att
        cont += 1
        # print(t, o, l)
        # assert(l==o)

    pprint(tdict)



if __name__ == "__main__":
    main()
