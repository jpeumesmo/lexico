'''
* ----------------------------------------------------------------------------
* "THE BEER-WARE LICENSE" (Revision 42):
* <joaopmoferreira@gmail.com> wrote this file. As long as you retain this notice
* you can do whatever you want with this stuff. If we meet some day, and you
* think this stuff is worth it, you can buy me a beer in return, Joao Pedro
* Moreira Ferreira
* ----------------------------------------------------------------------------
'''
import re,sys,os
from gramatica import *

##############################TABELAS########################################
tokens = []
identificadores = []
numerais = []
literais = []
separadores = []
reservadas = []
operadores = []
includes = []

listaReservadas = [ 'int', 'float', 'char','if', 'for', 'while','return'
,'break','continue','else'  ]
################################ABERTURA DO ARQ##############################
codigoFonte = open(sys.argv[1], 'r')

path = sys.path[0]

os.system("rm -rf saida")
os.system("mkdir saida")

saidaId = open(path+"/saida/identificadores.txt", 'w')
saidaNum = open(path+"/saida/numerais.txt", 'w')
saidaLit = open(path+"/saida/literais.txt", 'w')
saidaSep = open(path+"/saida/separadores.txt", 'w')
saidaRes = open(path+"/saida/reservadas.txt", 'w')
saidaOp = open(path+"/saida/operadores.txt", 'w')
saidaIncl = open(path+"/saida/inclues.txt", 'w')
saidaToken = open(path+"/saida/tokens.txt",'w')



########################VARIAVEIS CONTADORAS E AUXILIARES#####################
contLinha = 1
contColuna = 0
token = ""

############################LOOP PRINCIPAL###################################

caracter = codigoFonte.read(1)
contColuna = contColuna + 1
if caracter == "": #ARQ VAZIO
    pass
else:
    while True:
        token = ""


        if caracter == "": #END OF FILE
            break


        if re.match("\d",caracter) is not None:
            #####NUMERAL ENCONTRADO#########
            token = token + caracter
            flag = 0
            while True:
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
                if re.match("\d",caracter) is not None:
                    token = token + caracter
                elif re.match("\.",caracter) is not None and flag == 0:
                    flag = 1
                    token = token + caracter
                elif re.match("\n",caracter):
                    contLinha = contLinha + 1
                    contColuna = 0
                else:
                    numerais.append([token,contLinha,contColuna])
                    tokens.append([token,contLinha,contColuna,0,"NUM"])
                    break;

        elif re.match("\"",caracter) is not None:
            ###########LITERAL ENCONTRADO##################
            token = token + caracter
            while True:
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
                if re.match("\"",caracter) is not None:
                    token = token + caracter
                    literais.append([token,contLinha,contColuna])
                    tokens.append([token,contLinha,contColuna,1,"LIT"])
                    caracter = codigoFonte.read(1)
                    contColuna = contColuna + 1
                    break
                elif re.match("\n",caracter):
                    contLinha = contLinha + 1
                    contColuna = 0
                else:
                    token = token + caracter
        elif re.match("\<|\>",caracter) is not None:
            ############OPERACAO LOGICA ENCOTRADA############
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\=",caracter) is not None:
                token = token + caracter
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1

        elif re.match("\!",caracter) is not None:
            ###########OPERADOR DE DIFERENTE LOGICO ENCONTRADO######
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\=",caracter) is not None:
                token = token + caracter
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                sys.exit("Erro! linha %d, coluna %d"%(contLinha,contColuna) )

        elif re.match("\&",caracter) is not None:
            ##########ADN LOGICO ENCONTRADO#############
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\&",caracter) is not None:
                token = token + caracter
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                sys.exit("Erro! linha %d, coluna %d"%(contLinha,contColuna) )

        elif re.match("\|",caracter) is not None:
            ############# OU LOGICO ENCONTRADO###########
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\|",caracter) is not None:
                token = token + caracter
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                sys.exit("Erro! linha %d, coluna %d"%(contLinha,contColuna) )

        elif re.match("\=",caracter) is not None:
            ############ATRIBUICAO OU EQUIVALENCIA ENCONTRADA#########
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\=",caracter) is not None:
                token = token + caracter
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])
        elif re.match("\+",caracter):
            #############SOMA OU INCREMENTO ENCONTRADO###############
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\+",caracter) is not None:
                token = token + caracter
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])

        elif re.match("\-",caracter):
            ###########SUBTRACAO OU DECREMENTO ENCONTRADO############
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\-",caracter) is not None:
                token = token + caracter
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1

            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])

        elif re.match("\*|\^",caracter) is not None:
            ###########OPERACAO ARITIMETICA ENCONTRADA##############
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("[a-z]|[A-Z]|\_",caracter) is not None: #DIVISAO
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                sys.exit("Erro! linha %d, coluna %d"%(contLinha,contColuna) )
        elif re.match("\/",caracter) is not None:
            ################COMENTARIO OU DIVISAO ENCONTRADO###################
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\/",caracter) is not None: #COMENTARIO DE LINHA
                while True:
                    caracter = codigoFonte.read(1)
                    if re.match("\n",caracter):
                        contLinha = contLinha + 1
                        contColuna = 0
                        caracter = codigoFonte.read(1)
                        contColuna = contColuna + 1
                        break
            elif re.match("\*",caracter) is not None: #COMENTARIO DE BLOCO
                while True:
                    caracter = codigoFonte.read(1)
                    contColuna = contColuna + 1
                    if re.match("\n",caracter):
                        contLinha = contLinha + 1
                        contColuna = 0
                    if re.match("\*",caracter) is not None:
                        caracter = codigoFonte.read(1)
                        if re.match("\/",caracter) is not None:
                            caracter = codigoFonte.read(1)
                            break
            elif re.match("[a-z]|[A-Z]|\_|\ ",caracter) is not None: #DIVISAO
                operadores.append([token,contLinha,contColuna])
                tokens.append([token,contLinha,contColuna,2,"OP"])

            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                sys.exit("Erro! linha %d, coluna %d"%(contLinha,contColuna) )

        elif re.match("\;|\[|\]|\(|\)|\{|\}|\,",caracter) is not None:
        ##################SEPARADOR ENCONTRADO####################
            token = token + caracter
            separadores.append([token,contLinha,contColuna])
            tokens.append([token,contLinha,contColuna,3,"SEP"])
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1

        elif re.match("\n",caracter) is not None:
            contLinha = contLinha + 1
            contColuna = 0
            caracter = codigoFonte.read(1)
            contColuna =  contColuna + 1

        elif re.match("\ ",caracter) is not None:
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1

        elif re.match("\.",caracter) is not None:
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1

        elif re.match("\#",caracter) is not None:
            token = token + caracter
            while True:
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
                if re.match("\>",caracter) is not None:
                        token = token + caracter
                        includes.append([token,contLinha,contColuna])
                        tokens.append([token,contLinha,contColuna,4,"INCLU"])
                        caracter = codigoFonte.read(1)
                        contColuna = contColuna + 1
                        break
                elif re.match("\n",caracter) is not None:
                    contLinha = contLinha + 1
                    contColuna = 0
                else:
                    token = token + caracter
        elif re.match("[a-z]|[A-Z]|\_",caracter) is not None:
        ###############IDENTIFICADOR OU PALAVRA RESERVADA ENCONTRADA######
            token = token + caracter
            while True:
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
                if re.match("[a-z]|[A-Z]|\_",caracter) is not None:
                    token = token + caracter
                elif re.match("\n",caracter):
                    contLinha = contLinha + 1
                    contColuna = 0
                else:
                    if (token in listaReservadas):
                        identificadores.append([token,contLinha,contColuna])
                        tokens.append([token,contLinha,contColuna,6,"RESERVADA"])
                    else:
                        identificadores.append([token,contLinha,contColuna])
                        tokens.append([token,contLinha,contColuna,5,"ID"])
                    break

        else:
            sys.exit("Erro! linha %d, coluna %d"%(contLinha,contColuna) )


for i in identificadores:
        if(i[0] in listaReservadas):
            reservadas.append(i)
            identificadores.remove(i)


saidaToken.write("Classes:\n0 - numerais\n1 - literais\n2 - operacao\n3 - separador\n4 - includes\n5 - identificadores\n6 - reservada\n")
saidaToken.write("###################################################################################\n")
saidaToken.write("Token\tLinha\tColuna\tCodigo\tClasse\n-----------------------------------\n")
cont = 0
for i in tokens:
    saidaToken.write(str(cont)+"\t")
    for j in i:
        saidaToken.write(str(j)+"\t")
    saidaToken.write("\n")
    cont = cont + 1
saidaRes.write("Token \t Linha \t Coluna \n-----------------------------------\n")
for i in reservadas:
    for j in i:
        saidaRes.write(str(j)+"\t")
    saidaRes.write("\n")

saidaId.write("Token \t Linha \t Coluna \n-----------------------------------\n")
for i in identificadores:
    for j in i:
        saidaId.write(str(j)+"\t")
    saidaId.write("\n")

saidaNum.write("Token \t Linha \t Coluna \n-----------------------------------\n")
for i in numerais:
    for j in i:
        saidaNum.write(str(j)+"\t")
    saidaNum.write("\n")

saidaLit.write("Token \t Linha \t Coluna \n-----------------------------------\n")
for i in literais:
    for j in i:
        saidaLit.write(str(j)+"\t")
    saidaLit.write("\n")

saidaSep.write("Token \t Linha \t Coluna \n-----------------------------------\n")
for i in separadores:
    for j in i:
        saidaSep.write(str(j)+"\t")
    saidaSep.write("\n")

saidaOp.write("Token \t Linha \t Coluna \n-----------------------------------\n")
for i in operadores:
    for j in i:
        saidaOp.write(str(j)+"\t")
    saidaOp.write("\n")

saidaIncl.write("Token \t Linha \t Coluna \n-----------------------------------\n")
for i in includes:
    for j in i:
        saidaIncl.write(str(j)+"\t")
    saidaIncl.write("\n")

saidaId.close()
saidaNum.close()
saidaLit.close()
saidaSep.close()
saidaRes.close()
saidaOp.close()
saidaIncl.close()
saidaToken.close()

codigoFonte.close()

i = sintatico(tokens,-1)
print("fim")
