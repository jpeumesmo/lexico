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
tokens = []
identificadores = []
numerais = []
literais = []
separadores = []
reservadas = []

################################ABERTURA DO ARQ##############################
codigoFonte = open(sys.argv[1], 'r')

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
                else if re.match("\.",caracter) is not None and flag == 0:
                    flag = 1
                    token = token + caracter
                else:
                    numerais.append(token)
                    break;
        else if re.match("\"",caracter) is not None:
            ###########LITERAL ENCONTRADO##################
            token = token + caracter
            while True:
                caracter = codigoFonte.read(1)
                if re.match("\"",caracter) is not None:
                    token = token + caracter
                    literais.append(token)
                    break
                else:
                    token = toke + caracter
        else if re.match("\<|\>|\&|\!|\|",caracter) is not None:
            ############OPERACAO LOGICA ENCOTRADA############

        else if re.match("\=",caracter) is not None:
            ############ATRIBUICAO OU EQUIVALENCIA ENCONTRADA#########

        else if re.match("\+|\-|\*|\^|\\",caracter) is not None:
            ###########OPERACAO ARITIMETICA ENCONTRADA##############

        else if re.match("\/",caracter) is not None:
            ################COMENTARIO ENCONTRADO###################
            caracter = codigoFonte.read(1)
            if re.match("\/",caracter) is not None: #COMENTARIO DE LINHA
                while True:
                    caracter = codigoFonte.read(1)
                    if (caracter == "\n")
                        contLinha = contLinha + 1
                        break
            if re.match("\*",caracter) is not None: #COMENTARIO DE BLOCO
                while True:
                    caracter = codigoFonte.read(1)
                    if re.match("\*",caracter) is not None:
                        caracter = codigoFonte.read(1)
                        if re.match("\/",caracter) is not None:
                            break

        else if re.match("\;|\[|\(|\{|\,|.")
        ##################SEPARADOR ENCONTRADO####################
            token = token + caracter
            separadores.appen(token)

        else if: re.match("[a-z]|[A-Z]|\_",caracter)
        ###############IDENTIFICADOR OU PALAVRA RESERVADA ENCONTRADA
        else:
            print("Erro!")
print (numerais)
