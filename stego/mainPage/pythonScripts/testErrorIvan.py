import os
import random
import time


# CONFIGURATION VARIABLES
NUM_LINES = 5

# FUNCTIONS


def remove_line_html(html,number_lines) :
    random.seed(time.process_time())
    lin=list(html)
    print(lin)
    lines=[]
    for ind in range(number_lines):
        rand=random.randint(0,len(lin))
        lines.append(rand)

    lines.sort()
    count=0
    html_noline=""
    for index in range(len(lin)):
        if(count<number_lines):
            if index!=lines[count] :
                html_noline+=lin[index]
            else:
                count+=1
        else:
            html_noline+=lin[index]

    return html_noline


def main():

    with open(os.getcwd()+"/stego/responseContent.html") as fd:
        html = fd.read()

    newhtml = remove_line_html(html, NUM_LINES)



    assert len(html.splitlines()) == (len(newhtml.splitlines())+NUM_LINES)


if __name__ == "__main__":
    main()
