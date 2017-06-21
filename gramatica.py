def sintatico(token,i):
	programa(token,i)
	return i
def programa(token,i):

	if (token[i][3] == 5):
		i = atribuicao(token,i)
		i = programa(token,i)
		return i

	elif(token[i][0] == "int" or token[i][0] == "float" or token[i][0] == "char"):
		i = declaracao(token,i)
		return i
	else:
		return i

def declaracao(token,i):
	if (token[i][4] == 5):
		i =nextSimb(i)
		if (token[i][0] == ","):
			i = dec2(token,i)
			return i

		elif(token[i][0] == ";"):
			return i
		else:
			erro(i,"declaracao",token)
def atribuicao(token,i):
	if(token[i][0] == "="):
		i = E(exp,i)
		if(token[i][0] == ";"):
			return i
	else:
		erro(i,"atribuicao",token)
		return i

def E(token,i):
	if ((token[i][4]==5 or token[i][4]==1 or token[i][4]==0) or (token[i][0]=="(")):
		i = T(token,i)
		i = Elinha(token,i)
		return i
	else :
        	erro(i,"E",token)
		return i
def T(token,i):
	if(token[i][4]==5 or token[i][4]==1 or token[i][4]==0  or  token[i][0]=="(" ):
		i = F(token,i)
		i = Tlinha(token,i)
		return i
	else:
		erro(i,"T",token)
		return i

def Tlinha(token,i):
	if(token[i][0]=="+" or token[i][0]==")" or token[i][0]=="$" or token[i][0]== "-"):
		return i
	elif(token[i][0]=="*" or token[i][0]=="/"):
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
	elif(token[i][4]==5 or token[i][4]==1 or token[i][4]==0):
		i = nextSimb(i)
		return i
	else:
		erro(i,"F",token)
		return i


def Elinha(token,i):
	if(token[i][0] == "+" or token[i][0]=="-"):
		i = nextSimb(i)
		i =T(token,i)
		i = Elinha(token,i)
		return i
	elif (token[i][0]==")" or  token[i][0]=="$"):
		return i
	else:
		erro(i,"Elinha",token)
		return i

def erro(i,flag,token):
    print("Erro" , i, flag, token[i][0])
    return

def nextSimb(i):
    i = i + 1
    return i
