import re
import os
from codification_commas import insertar_comillas
from codification_spaces import insertar_tags
from decodification_spaces import retrieve_msg_spaces
from decodification_commas import retrieve_msg_commas



def main():


    payloadmsg_quotes = "1001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111001100010010110001110011100010100100000001100111111111101101110101110"
    print(list(payloadmsg_quotes))

    with open("./input.html") as fd:
        html = fd.read()


    # ENCODE pyaload msg multiple times with quotes codification
    newhtml = []
    for line in html.splitlines():

        newline = insertar_comillas(line, list(payloadmsg_quotes))
        newhtml.append(newline)


    print("\n".join(newhtml))
    ### QUOTATION MARKS
    msg_commas = []
    for line in newhtml:
        bits = retrieve_msg_commas(line)
        if(len(bits)>0):
            msg_commas += bits


    print("".join(msg_commas))
    print(payloadmsg_quotes == "".join(msg_commas))



if __name__ == "__main__":
    main()
