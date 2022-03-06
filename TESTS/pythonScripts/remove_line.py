import os
import random
import time

# TEMP*** Ivan function does not work fine
# def remove_line_html(html,number_lines) :
# 	random.seed(time.process_time())
# 	lines=[random.randint(0,len(html))]
# 	i=1
# 	while i<number_lines:
# 		rand=random.randint(0,len(html))
# 		if rand not in lines:
# 			lines.append(rand)
# 			i+=1
# 	lines.sort()
# 	print(lines)
# 	count=0
# 	html_noline=""
# 	index=0
# 	for linea in html:
# 		if(count<number_lines):
# 			if index!=lines[count] :
# 				html_noline+=linea
# 			else:
# 				count+=1
# 		else:
# 			html_noline+=linea
# 		index+=1
#
# 	return html_noline

def remove_line_html(html,number_lines) :

    htmllines = html.splitlines()

    for line in range(number_lines):
        current = len(htmllines)
        random.seed(time.process_time())
        r = random.randint(0,len(htmllines)-1)
        del htmllines[r]

        now = len(htmllines)
        if(current!=(now+1)):
            print(r)

    return "\n".join(htmllines)
