
import os



def num_attributes_line(line):

    maxlines = 0

    # See that is not a comment
    if((line.find("<!--")==-1) and (line.find("< !--")==-1)):

        words = line.split(" ")

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

    # with open(os.getcwd()+"/stego/responseContent.html") as fd:
    #     content = fd.read()
    #
    # hlines = content.splitlines()
    # # num_bits = count_bits(content)
    #
    # print(type(hlines))
    # print(hlines)

    test = [
        "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\">", # 2
        "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\" >",
        "< link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\">",
        "<link href=\"/static/vendor/owl.carousel/assets/owl.carousel.min.css\" rel=\"stylesheet\" >",
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
    ]



    for t,o in zip(test, output):

        l = num_attributes_line(t)
        print(t, o, l)
        assert(l==o)





if __name__ == "__main__":
    main()
