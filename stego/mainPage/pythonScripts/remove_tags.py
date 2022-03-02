def eliminar_tags(linea_html) :
	borrados_apertura=0
	lin=list(linea_html)
	for index in range(len(lin)):
		if(lin[index-borrados_apertura] == '<'):
			while(lin[index-borrados_apertura+1] == ' '):
				lin.pop(index-borrados_apertura+1)
				borrados_apertura+=1
		elif(lin[index-borrados_apertura] == '>') :
			while(lin[index-borrados_apertura-1] == ' '):
				lin.pop(index-borrados_apertura-1)
				borrados_apertura+=1
		
	linea_html_tags=""
	for j in range(len(lin)):
		linea_html_tags+=lin[j]
		
	return linea_html_tags
