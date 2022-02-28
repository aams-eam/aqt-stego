
'''CONTADOR NUMERO DE TAGS EN FICHERO'''
def contadortags(linestags):
	contadortags=0	
	lin=list(linestags)
	for index in range(len(lin)):
		if (lin[index] == '<')or (lin[index] == '>'):
			contadortags+=1
	return contadortags	

'''CONTADOR NUMERO COMILLAS EN FICHERO'''
def contadorcomillas(linescomillas):
	contadorcomillas=0
	lin=list(linescomillas)
	for index in range(len(lin)):
		if ((lin[index] == '"' )or (lin[index] == "'")):
			contadorcomillas+=1
	return int(contadorcomillas/2)
