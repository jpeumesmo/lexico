import re,sys
from gera import *

variaveis = []
statement = []
contVariaveis = 0
tipo1 = None
tipo2 = None
valido = None
operacao = None
falha = 0
contLabel = 1
operacoes = ["==","+","-","||",">","<","!=","<=",">=","*","/","&&"]

def sintatico(token,i):
	token.append(['$',None,None,7,'END'])
	i = programa(token,i)
	if (falha == 0):
		fim()
	return i

def programa(token,i):
	i = nextSimb(i)
	if (token[i][3] == 5):
		i = nextSimb(i)
		i = atribuicao(token,i)
		i = programa(token,i)
		return i

	elif(token[i][0] == "$"):
		return i
	elif(token[i][0] == "int" or token[i][0] == "float" or token[i][0] == "char"):
		i = declaracao(token,i)
		i = programa(token,i)
		return i

	elif(token[i][0] == "while"):
		i = repeticao(token,i)
		i = programa(token,i)
		return i

	elif(token[i][0] == "if"):
		i = condicao(token,i)
		i = programa(token,i)
		return i
	else:
		return i

def condicao(token,i):
	global contVariaveis
	global contLabel
	i = nextSimb(i)
	if (token[i][0] == "("):
		i = nextSimb(i)
		i = E(token,i)
		if(not valido):
			erro(i,"operacao",token)
		geraCod("Load $t"+str(contVariaveis)+","+token[i-1][0])
		if (token[i][0] == ")"):
			i = nextSimb(i)
			if (token[i][0] == "{"):
				geraCod("bne "+"1,"+"$t"+str(contVariaveis)+" label"+str(contLabel))
				contVariaveis = contVariaveis + 1
				i = programa(token,i)
				if (token[i][0] == "}"):
					geraCod("label"+str(contLabel))
					contLabel = contLabel + 1
					return i
				else:
					erro(i,"condicao",token)
			else:
				erro(i,"condicao",token)
		else:
			erro(i,"condicao",token)
	else:
		erro(i,"condicao",token)

def repeticao(token,i):
	global contVariaveis
	global contLabel

	i = nextSimb(i)
	if(token[i][0]== "("):
		i = nextSimb(i)
		i = E(token,i)
		if(not valido):
			erro(i,"operacao",token)
		geraCod("Load $t"+str(contVariaveis)+","+token[i-1][0])
		if (token[i][0] == ")"):
			i = nextSimb(i)
			if (token[i][0] == "{"):
				geraCod("bne "+"1,"+"$t"+str(contVariaveis)+" label"+str(contLabel))
				contVariaveis = contVariaveis + 1
				i = programa(token,i)
				if (token[i][0] == "}"):
					geraCod("label"+str(contLabel))
					contLabel = contLabel + 1
					return i
				else:
					erro(i,"repeticao",token)
			else:
				erro(i,"repeticao",token)
		else:
			erro(i,"repeticao",token)
	else:
		erro(i,"repeticao",token)

def declaracao(token,i):
	global variaveis
	global statement
	global contVariaveis

	statement = []
	statement.append(token[i][0])
	i = nextSimb(i)
	if (token[i][3] == 5):
		statement.append(token[i][0])
		i = nextSimb(i)
		if(token[i][0] == ";"):
			flagDeclarada = 0
			for v in variaveis:
				if (statement[1] in v[1]):
					flagDeclarada = 1
					break
			if (flagDeclarada == 0):
				variaveis.append(statement)
				geraCod("Store $t"+str(contVariaveis)+","+token[i-1][0])
				contVariaveis = contVariaveis + 1

	else:
		erro(i,"declaracao",token)
	return 	i

def atribuicao(token,i):
	global variaveis
	global statement
	global contVariaveis
	global valido

	statement = []
	statement.append(None)
	statement.append(token[i][0])

	if (len(variaveis) == 0):
		erro(i,"nodeclared",token)
	else:
		flagDeclarada = 0
		if (statement[1] == "="):
			flagDeclarada = 1
		for v in variaveis:
			if (statement[1] in v[1]):
				flagDeclarada = 1
				break
		if (flagDeclarada == 0):
			erro(i,"nodeclared",token)

	if(token[i][0] == "="):
		i = nextSimb(i)
		i = E(token,i)
		if(not valido):
			erro(i,"operacao",token)
		geraCod("Load $t"+str(contVariaveis)+","+token[i-1][0])
		contVariaveis = contVariaveis + 1

		if(token[i][0] == ";"):

			return i
	else:
		erro(i,"atribuicao",token)
		return i

def E(token,i):
	global tipo1
	global tipo2
	global valido

	if ((token[i][3]==5 or token[i][3]==1 or token[i][3]==0) or (token[i][0]=="(")):
		i = T(token,i)
		i = Elinha(token,i)
		if (tipo1[0] == tipo2[0]):
			valido = True
		return i
	else :
        	erro(i,"E",token)
		return i
def T(token,i):
	global tipo1
	global tipo2
	global operacao
	global operacoes
	if(token[i][3]==5 or token[i][3]==1 or token[i][3]==0  or  token[i][0]=="(" ):
		i = F(token,i)
		i,op = Tlinha(token,i)

		if(tipo2 is None ):
			operacao = op
		elif (op == ")" or op == ";"):
			operacao = operacao
		else:
			flag = 0
			if(op in operacoes):
				flag = 1
				geraCod(str(op)+" "+str(tipo1[1])+","+str(tipo2[1]))
			elif (operacao in operacoes and flag == 0):
				geraCod(str(operacao)+" "+str(tipo1[1])+","+str(tipo2[1]))

		return i
	else:
		erro(i,"T",token)
		return i

def Tlinha(token,i):
	op = token[i][0]
	if(token[i][0]=="+" or token[i][0]==")" or token[i][0]==";" or token[i][0]== "-" or token[i][0]== "||"
	 or token[i][0]== ">" or token[i][0]== "<"  or token[i][0]== "=="  or token[i][0]== "!="
	 or token[i][0]== "<="  or token[i][0]== ">="):
		return i,op
	elif(token[i][0]=="*" or token[i][0]=="/" or token[i][0]== "&&"):
		i = nextSimb(i)
		i = F(token,i)
		i = Tlinha(token,i)
		return i,op
	else:
		erro(i,"Tlinha",token)
		return i,op
def F(token,i):
	global contVariaveis
	global tipo1
	global tipo2
	global variaveis

	if (token[i][0] == "("):
		i = nextSimb(i)
        	i = E(token,i)
        	i = nextSimb(i)
		return i

        	if(token[i][0] != ")"):
	   		erro(i,"F",token)
	   		return i
	elif(token[i][3]==5 or token[i][3]==1 or token[i][3]==0):
		for v in variaveis:
			if (v[1] == token[i][0]):
				if (tipo1 is None):
					tipo1 = v
				else:
					tipo2 = tipo1
					tipo1 = v
		i = nextSimb(i)
		return i
	else:
		erro(i,"F",token)
		return i,None


def Elinha(token,i):
	if(token[i][0] == "+" or token[i][0]=="-" or token[i][0]== "||"
	or token[i][0]== ">" or token[i][0]== "<"  or token[i][0]== "=="  or token[i][0]== "!="
	or token[i][0]== "<="  or token[i][0]== ">="):
		i = nextSimb(i)
		i =T(token,i)
		i = Elinha(token,i)
		return i
	elif (token[i][0]==")" or  token[i][0]==";"):
		return i
	else:
		erro(i,"Elinha",token)
		return i

def erro(i,flag,token):
	#print("Erro" , i, flag, token[i][0])
	global falha
	falha = 1
	if (flag == "dupla"):
		j = i - 1
		sys.exit("Erro dupla declaracao de variavel "+token[j][0] +" linha: "+str(token[j][1])+" coluna: "+str(token[j][2]))
	elif (flag == "nodeclared"):
		j = i - 1
		sys.exit("Erro variavel nao declarada "+token[j][0] +" linha: "+str(token[j][1])+" coluna: "+str(token[j][2]))
	elif(flag == "operacao"):
		sys.exit("Erro operacao invalida ")
	else:
		sys.exit("Erro token:"+token[i][0]+"\tlinha: "+str(token[i][1])+"\tcoluna: "+str(token[i][2]))


def nextSimb(i):
    i = i + 1
    return i
