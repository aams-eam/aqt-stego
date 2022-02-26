import math
import sys

'''ABRO FICHERO PARA LEER'''
file = "./stego/responseContent.html"
f = open(file, 'r')

'''LEO FICHERO'''
contenido=f.readlines()

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
print(entrada_codificada)

'''VARIABLES PARA GUARDAR EL HTML MODIFICADO DE COMILLAS Y TAGS'''
html_tags_lista=[]



'''INSERTAR ESPACIOS SEGUN LA ENTRADA'''
def insertar_tags(array_codificado) :
	inde=0
	for lines in contenido:
		lin=list(lines)
		for index in range(len(lin)):
			if lin[index] == '<':
				if(inde<len(array_codificado)):
					if(array_codificado[inde] == '1'):
						lin.insert(index+1,' ')
						inde+=1
					else:
						inde+=1
			elif (lin[index] == '>') and (lin[index-1] != ' '):
					if(inde<len(array_codificado)):
						if(array_codificado[inde] == '1'):
							lin.insert(index,' ')
							inde+=1
						else:
							inde+=1

		html_tags_lista.append(lin)
	html_tags=""
	for b in range(len(html_tags_lista)):
		straux=""
		for j in range(len(html_tags_lista[b])):
			straux+=html_tags_lista[b][j]
		html_tags+=straux
	return html_tags

devolver2=insertar_tags(entrada_codificada)
print(devolver2)


# ALEJANDRO TEST
import os
with open(os.getcwd()+"/stego/tempResponseAlejandro.html", 'w') as fd:
    fd.write(devolver)
