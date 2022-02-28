from counter_bytes_tags import contadortags


'''TAGS SEGUN ENTRADA'''

def insertar_tags(linea_html,entrada_codificada) :
	inde=0
	insertados=0
	lin=list(linea_html)
	bits_tags= contadortags(linea_html)
	for index in range(len(lin)):
		if lin[index+insertados] == '<':
			if((len(entrada_codificada))!=0):
				if(inde<bits_tags):
					if(entrada_codificada[0] == '1'):
						lin.insert(index+insertados+1,' ')
						entrada_codificada.pop(0)
						inde+=1
					else:
						entrada_codificada.pop(0)
						inde+=1
		elif (lin[index+insertados] == '>') and (lin[index+insertados-1] != ' '):
			if((len(entrada_codificada))!=0):
				if(inde<len(entrada_codificada)):
					if(entrada_codificada[0] == '1'):
						lin.insert(index+insertados,' ')
						entrada_codificada.pop(0)
						insertados+=1
						inde+=1
					else:
						entrada_codificada.pop(0)
						inde+=1

	linea_html_tags=""
	for j in range(len(lin)):
		linea_html_tags+=lin[j]

	return linea_html_tags
