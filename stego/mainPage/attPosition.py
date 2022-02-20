import os
import re
from pprint import pprint
from bs4 import BeautifulSoup


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

            # --- OBTAIN AL EXISTENT ATTRIBUTES --->
            if(content.find("< ") >= 0):
                content = content.replace("< ", "<")

            if(content.find(" >") >= 0):
                content = content.replace(" >", ">")

            soup = BeautifulSoup(content, 'html.parser')
            # [tag.attrs for tag in soup.findAll('a')]
            try:
                att = soup.find_all()[0].attrs
                maxlines = len(att)
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



def tests():

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
            '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d22864.11283411948!2d-73.96468908098944!3d40.630720240038435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sbg!4v1540447494452" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen>',
            '< iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d22864.11283411948!2d-73.96468908098944!3d40.630720240038435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sbg!4v1540447494452" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen>',
            '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d22864.11283411948!2d-73.96468908098944!3d40.630720240038435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sbg!4v1540447494452" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen >',
            '< iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d22864.11283411948!2d-73.96468908098944!3d40.630720240038435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY%2C+USA!5e0!3m2!1sen!2sbg!4v1540447494452" width="100%" height="380" frameborder="0" style="border:0" allowfullscreen >',
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

        for t,o in zip(test, output):

            num_att = num_attributes_line(t)
            print(t, o, num_att)
            assert(o==num_att)

if __name__ == "__main__":
    # tests()
    main()
