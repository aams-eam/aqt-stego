import sys

def codificar_mensaje():
	mensajeaux=""
	for index in range(len(sys.argv)):
		if(index!=0):
			mensajeaux+=sys.argv[index]+' '
	byte_list=[bin(byte)[2:].zfill(8) for byte in bytearray(mensajeaux,"utf8")]
	res=[bit for byte in byte_list for bit in byte]
	return res
	
