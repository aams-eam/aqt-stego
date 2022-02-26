
import math
import sys

'''ABRO FICHERO PARA LEER'''
f = open("./stego/mainPage/templates/mainPage/indexExpanded.html", 'r')

'''LEO FICHERO'''
contenido=f.readlines()

'''VARIABLES PARA ALMACENAR EL TOTAL DE BYTES QUE CABEN USANDO LOS TAGS Y LAS COMILLAS'''
byte_tags=0
byte_comillas=0

'''VARIABLE PARA GUARDAR LA ENTRADA CODIFICADA'''
entrada_codificada=[]

'''VARIABLES PARA ALMACENAR EL TAMANIO DE LA ENTRADA Y LOS BYTES QUE QUEDAN POR CODIFICAR'''
bytestotales=0
bytesrestantes=0


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

'''ACTUALIZO EL TAMANIO DE LA ENTRADA Y LOS BYTES RESTANTES'''
bytestotales=math.floor((len(entrada_codificada))/8)
bytesrestantes=bytestotales

'''CONTADOR NUMERO DE TAGS EN FICHERO'''
def contadortags():
	contadortags=0
	for lines in contenido:
		lin=list(lines)
		for index in range(len(lin)):
			if (lin[index] == '<')or (lin[index] == '>'):
				contadortags+=1
	return math.floor(contadortags/8)

'''CONTADOR NUMERO COMILLAS EN FICHERO'''
def contadorcomillas():
	contadorcomillas=0
	for lines in contenido:
		lin=list(lines)
		for index in range(len(lin)):
			if (lin[index] == '"'):
				contadorcomillas+=1
	return math.floor(contadorcomillas/8)

'''CONTADOR TOTAL COMILLAS Y TAGS'''
def contadortotal():
	com=contadorcomillas()
	tagcont=contadortags()
	return com+tagcont

'''CALCULO LOS BYTES Y LOS TAGS QUE CABEN EN EL HTML'''
byte_tags=contadortags()
byte_comillas=contadorcomillas()

'''VARIABLES PARA GUARDAR EL HTML MODIFICADO DE COMILLAS Y TAGS'''
html_comillas_lista=[]
html_tags_lista=[]

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

'''TAGS SEGUN ENTRADA'''
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

'''FUNCION QUE ORGANIZA LA DISTRIBUCION DE LA ENTRADA EN TAGS Y COMILLAS SI ES NECESARIO'''
def codificar() :
	devolv=""
	if((byte_tags) >= (bytestotales)) :
		devolv=insertar_tags(entrada_codificada)
	else:
		devolv1=insertar_tags(entrada_codificada[0:byte_tags*8])
		bytesrestantes= (bytestotales) - (byte_tags)
		if(byte_comillas >= bytesrestantes) :
			print(entrada_codificada[(bytestotales*8)-(bytesrestantes*8):(bytestotales*8)])
			devolv=insertar_comillas(entrada_codificada[(bytestotales*8)-(bytesrestantes*8):(bytestotales*8)],devolv1)
		else:
			devolv=insertar_comillas(entrada_codificada[(bytestotales*8)-(bytesrestantes*8):((bytestotales*8)-(bytesrestantes*8))+(byte_comillas*8)],devolv1)
			bytesrestantes=bytesrestantes-byte_comillas
			print(bytesrestantes)
	return devolv

resultado=codificar()
print(resultado)
