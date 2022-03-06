import os
import random
import time


# CONFIGURATION VARIABLES
NUM_LINES = 5

# FUNCTIONS


def remove_line_html(html,number_lines) :
    random.seed(time.process_time())
    lines=[random.randint(0,len(html))] 
	i=1
	while i<number_lines:
		rand=random.randint(0,len(html))
		if rand not in lines:
			lines.append(rand)
			i+=1
	lines.sort()
	count=0
	html_noline=""
	index=0
	for linea in html:
		if(count<number_lines):
			if index!=lines[count] :
				html_noline+=linea
			else:
				count+=1
		else:
			html_noline+=linea
		index+=1
	
	return html_noline


def main():

    with open(os.getcwd()+"/stego/responseContent.html") as fd:
        html = fd.readlines()

    newhtml = remove_line_html(html, NUM_LINES)
    print(newhtml)



    '''assert len(html.splitlines()) == (len(newhtml.splitlines())+NUM_LINES)'''


if __name__ == "__main__":
    main()
