import sys

def sintatico(token,i):
	token.append(['$',None,None,7,'END'])
	i = programa(token,i)
	return i

def programa(token,i):
	i = nextSimb(i)
	if (token[i][3] == 5):
		i = nextSimb(i)
		i = atribuicao(token,i)
		i = programa(token,i)
		return i

	elif(token[i][3] == 7):
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
	i = nextSimb(i)
	if (token[i][0] == "("):
		i = nextSimb(i)
		i = E(token,i)
		if (token[i][0] == ")"):
			i = nextSimb(i)
			if (token[i][0] == "{"):
				i = programa(token,i)
				if (token[i][0] == "}"):
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
	return i

def declaracao(token,i):
	i = nextSimb(i)
	if (token[i][3] == 5):
		i = nextSimb(i)
		if (token[i][0] == ","):
			i = declaracao(token,i)

			return i

		elif(token[i][0] == ";"):
			return 	i
		else:
			erro(i,"declaracao",token)

def dec2(token,i):
	if (token[i][3] == 5):
		return i
	else:
		erro(i,"dec2",token)

def atribuicao(token,i):
	if(token[i][0] == "="):
		i = nextSimb(i)
		i = E(token,i)

		if(token[i][0] == ";"):
			return i
	else:
		erro(i,"atribuicao",token)
		return i

def E(token,i):
	if ((token[i][3]==5 or token[i][3]==1 or token[i][3]==0) or (token[i][0]=="(")):
		i = T(token,i)
		i = Elinha(token,i)
		return i
	else :
        	erro(i,"E",token)
		return i
def T(token,i):
	if(token[i][3]==5 or token[i][3]==1 or token[i][3]==0  or  token[i][0]=="(" ):
		i = F(token,i)
		i = Tlinha(token,i)
		return i
	else:
		erro(i,"T",token)
		return i

def Tlinha(token,i):
	if(token[i][0]=="+" or token[i][0]==")" or token[i][0]==";" or token[i][0]== "-" or token[i][0]== "||"
	 or token[i][0]== ">" or token[i][0]== "<"  or token[i][0]== "=="  or token[i][0]== "!="
	 or token[i][0]== "<="  or token[i][0]== ">="):
		return i
	elif(token[i][0]=="*" or token[i][0]=="/" or token[i][0]== "&&"):
		i = nextSimb(i)
		i = F(token,i)
		i = Tlinha(token,i)
		return i
	else:
		erro(i,"Tlinha",token)
		return i
def F(token,i):
	if (token[i][0] == "("):
		i = nextSimb(i)
        	i = E(token,i)
        	i = nextSimb(i)
		return i

        	if(token[i][0] != ")"):
	   		erro(i,"F",token)
	   		return i
	elif(token[i][3]==5 or token[i][3]==1 or token[i][3]==0):
		i = nextSimb(i)
		return i
	else:
		erro(i,"F",token)
		return i


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
	sys.exit("Erro token:"+token[i][0]+"\tlinha: "+str(token[i][1])+"\tcoluna: "+str(token[i][2]))

def nextSimb(i):
    i = i + 1
    return i
