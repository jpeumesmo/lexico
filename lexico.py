'''
* ----------------------------------------------------------------------------
* "THE BEER-WARE LICENSE" (Revision 42):
* <joaopmoferreira@gmail.com> wrote this file. As long as you retain this notice
* you can do whatever you want with this stuff. If we meet some day, and you
* think this stuff is worth it, you can buy me a beer in return, Joao Pedro
* Moreira Ferreira
* ----------------------------------------------------------------------------
'''
import re,sys

tokens = []
identificadores = []
numerais = []
literais = []
separadores = [" ","\n","\t"]
reservadas = [ ["int"], ['float'], ['char'],['if'], ['for'], ['while'],['return']
,['break'],['continue'],['else' ] ]

codigoFonte = open(sys.argv[1], 'r')
token = ""
contLinha = 0
contColuna = 0

while True:
    token = ""
    flag = 0
    while True:
        caracter = codigoFonte.read(1)
        contColuna = contColuna + 1
        #verificar os separadores
        for i in separadores:
            if ((caracter == i) or (caracter == "")):
                flag = 1
                if (caracter == "\n"):
                    contLinha = contLinha +1
                    contColuna = 0
        #break achou 1 token
        if flag == 1:
            break
        #montar token
        else:
            token = token+caracter

    #adiciona token a lista de tokens
    tokens.append([token,contLinha,contColuna])
    #break do end of file
    if caracter == "":
        break


    #verificacao se eh uma palavra reservadas

    contAux = 0
    for i in reservadas:
            for j in i:
                if token is j:
                    reservadas[contAux].append(contLinha)
                    reservadas[contAux].append(contColuna)
            contAux = contAux + 1;
    #expressao regular para indetificadores


    #expressao regular para numerais


    #expressao regular para literais



codigoFonte.close()
#print (reservadas[0][1])
for i in tokens:
    print (i)
