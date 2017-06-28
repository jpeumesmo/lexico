import sys

path = sys.path[0]
assembly = open(path+"/assembly.txt",'w')
codigo = []

def geraCod(comando):
#	global assembly
    global cont
    global codigo
    print(comando)
    codigo.append(comando)
    #assembly.write(comando+"\n")
    return

def fim():
    global assembly
    global codigo
    for c in codigo:
        assembly.write(str(c))
        assembly.write("\n")
    assembly.close()
