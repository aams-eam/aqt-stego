import sys
import os
from counter_bytes_tags import contadortags
from counter_bytes_tags import contadorcomillas
from message_codification import codificar_mensaje
from codification_commas import insertar_comillas
from codification_spaces import insertar_tags


with open(os.getcwd()+"\\responseContent.html") as fd:
    content = fd.readlines()


entrada_codificada=codificar_mensaje()
print('La entrada codificada es : \n', entrada_codificada)


print('En la linea 103 hay ',contadortags(content[102]), 'tags')
print('En la linea 39 hay ',contadorcomillas(content[38]), 'comillas')

'''print('CODIFICACION TAGS : \n')
for lines in content:
	print(insertar_tags(lines,entrada_codificada),' \n')'''
	
print('CODIFICACION COMILLAS : \n')
for lines in content:
	print(insertar_comillas(lines,entrada_codificada),' \n')
