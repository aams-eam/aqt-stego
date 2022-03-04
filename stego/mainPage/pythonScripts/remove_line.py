import os
import random
	
def remove_line_html(html,number_lines) :
	lin=list(html)
	lines=[]
	for ind in range(number_lines):
		rand=random.randint(0,len(lin))
		print(rand)
		lines.append(rand)
	lines.sort()
	count=0
	print(lines)
	html_noline=""
	for index in range(len(lin)):
		if(count<number_lines):
			if index!=lines[count] :
				html_noline+=lin[index]
			else:
				print(count)
				count+=1
		else:
			html_noline+=lin[index]
	
	return html_noline
