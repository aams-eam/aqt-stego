def eliminar_comillas(linea_html) :
	
	lin=list(linea_html)
	for index in range(len(lin)):
		if(lin[index] == "'"):
			lin[index]='"'
		
	linea_html_tags=""
	for j in range(len(lin)):
		linea_html_tags+=lin[j]
		
	return linea_html_tags
