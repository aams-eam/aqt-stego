
<<<<<<< HEAD
from counter_bytes_tags import contadorcomillas
=======
'''ABRO FICHERO PARA LEER'''
file = "./stego/responseContent.html"
f = open(file, 'r')

'''LEO FICHERO'''
contenido=f.readlines()

print(contenido)

'''VARIABLE PARA GUARDAR LA ENTRADA CODIFICADA'''
entrada_codificada=[]

def codificar_mensaje():
	mensajeaux=""
	for index in range(len(sys.argv)):
		if(index!=0):
			mensajeaux+=sys.argv[index]+' '
	byte_list=[bin(byte)[2:].zfill(8) for byte in bytearray(mensajeaux,"utf8")]
	res=[bit for byte in byte_list for bit in byte]
	return res

'''CODIFICO EL MENSAJE DE ENTRADA'''
entrada_codificada=codificar_mensaje()
print("MESSAGE: ", entrada_codificada)

'''VARIABLES PARA GUARDAR EL HTML MODIFICADO DE COMILLAS'''
html_comillas_lista=[]
>>>>>>> Added some modifications so the reading of the html files are acording to the repo, need to fix things in ISSUE #12, (Ivan Script Fixes)



'''INSERTAR COMILLAS SIMPLES O DOBLES SEGUN ENTRADA'''

def insertar_comillas(linea_html,entrada_codificada) :
	indic=0
<<<<<<< HEAD
	lin=list(linea_html)
	primer=0
	control=0
	bits_comillas= contadorcomillas(linea_html)
	for index in range(len(lin)):
		if lin[index] == '"':
			if((len(entrada_codificada))!=0):
				if(indic < bits_comillas):
=======

	for lines in contenido1:
		lin=list(lines)
		primer=0
		control=0
		for index in range(len(lin)):
			if lin[index] == '"':
				if((indic)<(len(array_con_tags))):
>>>>>>> Added some modifications so the reading of the html files are acording to the repo, need to fix things in ISSUE #12, (Ivan Script Fixes)
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
<<<<<<< HEAD
	linea_html_comillas=""	
	for j in range(len(lin)):
		linea_html_comillas+=lin[j]
	
	return linea_html_comillas
=======

		html_comillas_lista.append(lin)

	html_comillas=""
	for b in range(len(html_comillas_lista)):
		straux=""
		for j in range(len(html_comillas_lista[b])):
			straux+=html_comillas_lista[b][j]
		html_comillas+=straux
	return html_comillas

devolver=insertar_comillas(entrada_codificada,contenido)
print(devolver)


# ALEJANDRO TEST
import os
with open(os.getcwd()+"/stego/tempResponseAlejandro.html", 'w') as fd:
    fd.write(devolver)
>>>>>>> Added some modifications so the reading of the html files are acording to the repo, need to fix things in ISSUE #12, (Ivan Script Fixes)
