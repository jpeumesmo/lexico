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


##############################TABELAS########################################
identificadores = []
numerais = []
literais = []
separadores = []
reservadas = []
operadores = []

################################ABERTURA DO ARQ##############################
codigoFonte = open(sys.argv[1], 'r')
tabelas = open("/home/jpeumesmo/UFSJ/Compiladores/lexico/saida.txt", 'w')
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
                    numerais.append(token)
                    caracter = codigoFonte.read(1)
                    contColuna = contColuna + 1
                    break;

    #    elif re.match("\#",caracter) is not None:
            ############include encontrado#############
        elif re.match("\"",caracter) is not None:
            ###########LITERAL ENCONTRADO##################
            token = token + caracter
            while True:
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
                if re.match("\"",caracter) is not None:
                    token = token + caracter
                    literais.append(token)
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
                operadores.append(token)
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
                operadores.append(token)
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                sys.exit("Erro! 2" )

        elif re.match("\&",caracter) is not None:
            ##########ADN LOGICO ENCONTRADO#############
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\&",caracter) is not None:
                token = token + caracter
                operadores.append(token)
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                sys.exit("Erro! 3" )

        elif re.match("\|",caracter) is not None:
            ############# OU LOGICO ENCONTRADO###########
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\|",caracter) is not None:
                token = token + caracter
                operadores.append(token)
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                sys.exit("Erro! 4" )

        elif re.match("\=",caracter) is not None:
            ############ATRIBUICAO OU EQUIVALENCIA ENCONTRADA#########
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\=",caracter) is not None:
                token = token + caracter
                operadores.append(token)
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                operadores.append(token)
        elif re.match("\+",caracter):
            #############SOMA OU INCREMENTO ENCONTRADO###############
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\+",caracter) is not None:
                token = token + caracter
                operadores.append(token)
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                operadores.append(token)

        elif re.match("\-",caracter):
            ###########SUBTRACAO OU DECREMENTO ENCONTRADO############
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("\-",caracter) is not None:
                token = token + caracter
                operadores.append(token)
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
                break
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                operadores.append(token)

        elif re.match("\*|\^",caracter) is not None:
            ###########OPERACAO ARITIMETICA ENCONTRADA##############
            token = token + caracter
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1
            if re.match("[a-z]|[A-Z]|\_|\s",caracter) is not None: #DIVISAO
                operadores.append(token)
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
            else:
                sys.exit("Erro! 5" )
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
            elif re.match("[a-z]|[A-Z]|\_|\s",caracter) is not None: #DIVISAO
                operadores.append(token)
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            elif re.match("\n",caracter):
                contLinha = contLinha + 1
                contColuna = 0
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
            else:
                sys.exit("Erro! 6" )

        elif re.match("\;|\[|\]|\(|\)|\{|\}|\,",caracter) is not None:
        ##################SEPARADOR ENCONTRADO####################
            token = token + caracter
            separadores.append(token)
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1

        elif re.match("\n",caracter) is not None:
            contLinha = contLinha + 1
            contColuna = 0
            caracter = codigoFonte.read(1)
            contColuna = 0

        elif re.match("\s",caracter) is not None:
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1

        elif re.match("\.|\#",caracter) is not None:
            caracter = codigoFonte.read(1)
            contColuna = contColuna + 1

        elif re.match("[a-z]|[A-Z]|\_",caracter) is not None:
        ###############IDENTIFICADOR OU PALAVRA RESERVADA ENCONTRADA######
            token = token + caracter
            while True:
                caracter = codigoFonte.read(1)
                contColuna = contColuna + 1
                if re.match("[a-z]|[A-Z]|\_",caracter) is not None:
                    token = token + caracter
                else:
                    break
            if re.match("if|else|while|return|continue|break|int|char|float|for",token) is not None:
                reservadas.append(token)
            else:
                identificadores.append(token)

        else:
            sys.exit("Erro! 7 c %d l %d"%(contColuna,contLinha) )

for i in reservadas:
    tabelas.write(i+"\n")
tabelas.close()
print("fim")
