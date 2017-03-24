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



codigoFonte = open(sys.argv[1], 'r')

texto = codigoFonte.read(1)
print (texto)
#texto = codigoFonte.readlines()
#for linha in texto:
#    print (linha)


codigoFonte.close
