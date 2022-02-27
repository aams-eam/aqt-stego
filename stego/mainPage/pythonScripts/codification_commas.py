
from counter_bytes_tags import contadorcomillas



'''INSERTAR COMILLAS SIMPLES O DOBLES SEGUN ENTRADA'''

def insertar_comillas(linea_html,entrada_codificada) :
	indic=0
	lin=list(linea_html)
	primer=0
	control=0
	bits_comillas= contadorcomillas(linea_html)
	for index in range(len(lin)):
		if lin[index] == '"':
			if((len(entrada_codificada))!=0):
				if(indic < bits_comillas):
					if primer == 0 :
						if(entrada_codificada[0] == '1'):
							lin[index] = "'"
							control=1
							primer=1
						else:
							primer=1
					else :
						if(control == 1):
							lin[index] = "'"
							control=0
							primer=0
							entrada_codificada.pop(0)
							indic+=1
						else:
							primer=0
							entrada_codificada.pop(0)
							indic+=1
	linea_html_comillas=""	
	for j in range(len(lin)):
		linea_html_comillas+=lin[j]
	
	return linea_html_comillas
