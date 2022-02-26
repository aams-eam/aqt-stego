
<<<<<<< HEAD

from counter_bytes_tags import contadortags
=======
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
>>>>>>> Added some modifications so the reading of the html files are acording to the repo, need to fix things in ISSUE #12, (Ivan Script Fixes)


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
<<<<<<< HEAD
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
=======
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
>>>>>>> Added some modifications so the reading of the html files are acording to the repo, need to fix things in ISSUE #12, (Ivan Script Fixes)
