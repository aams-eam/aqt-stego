import math
import sys

'''ABRO FICHERO PARA LEER'''
f = open("C:\\Users\\Iván\\Downloads\\responseContent.html", 'r')

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

'''VARIABLES PARA GUARDAR EL HTML MODIFICADO DE COMILLAS'''
html_comillas_lista=[]



'''INSERTAR COMILLAS SIMPLES O DOBLES SEGUN ENTRADA'''
def insertar_comillas(array_con_tags,contenido1) :
	indic=0
	
	for lines in contenido1:
		lin=list(lines)
		primer=0
		control=0
		for index in range(len(lin)):
			if lin[index] == '"':
				if((indic)<(len(array_con_tags))):
					if primer == 0 :
						if((array_con_tags[indic]) == '1'):
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
							indic+=1
						else:
							primer=0
							indic+=1
		
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

