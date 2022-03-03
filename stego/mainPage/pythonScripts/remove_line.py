import os
import random
	
def remove_line(html) :
	lin=list(html)
	rand=random.randint(0,len(lin))
	print(rand)
	html_noline=""
	for index in range(len(lin)):
		if index!=rand :
			html_noline+=lin[index]
	
	return html_noline
