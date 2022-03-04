'''CONTADOR NUMERO DE TAGS EN FICHERO'''
def contadortags(linestags):
<<<<<<< HEAD
	contadortags=0
=======
	contadortags=0	
>>>>>>> 709e1878918df6c248144c86a80140ba774b0561
	lin=list(linestags)
	for index in range(len(lin)):
		if (((chr(lin[index])) == '<') or ((chr(lin[index])) == '>')):
			contadortags+=1
<<<<<<< HEAD
	return contadortags
=======
	return contadortags	
>>>>>>> 709e1878918df6c248144c86a80140ba774b0561

'''CONTADOR NUMERO COMILLAS EN FICHERO'''
def contadorcomillas(linescomillas):
	contadorcomillas=0
	lin=list(linescomillas)
	for index in range(len(lin)):
		if (((chr(lin[index])) == '"') or ((chr(lin[index])) == "'")):
			contadorcomillas+=1
	return int(contadorcomillas/2)
