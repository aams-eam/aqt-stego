import math
import sys

'''ABRO FICHERO PARA LEER'''
f = open("C:\\Users\\Iván\\Downloads\\responseContent.html", 'r')

'''LEO FICHERO'''
contenido=f.readlines()

'''VARIABLES PARA ALMACENAR EL TOTAL DE BYTES QUE CABEN USANDO LOS TAGS Y LAS COMILLAS'''
byte_tags=0
byte_comillas=0


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
print(byte_tags)
print(byte_comillas)
