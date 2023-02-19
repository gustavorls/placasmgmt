from multiprocessing import Process
import re
from placa_rewriteChar import *
from placa_rewriteDig import *
from placa_convertChar import *
from placa_convertDig import *

def mgmt():
	str = 'Escolha o que fazer:/nDigite 1 para rewriteChar/nDigite 2 para rewriteDig/nDigite 3 para convertChar/nDigite 4 para convertDig: '
	choose = int(input(re.sub(r'/n', r'\n', str)))
	if (choose >= 5):
		print('Entrada inválida.')
	else:
		print()
		placa = input("Informe a placa: ")
	
	if (choose == 1):
		RewriteChar(placa)
	elif (choose == 2):
		RewriteDig(placa)
	elif (choose == 3):
		ConvertToChar(placa)
	elif (choose == 4):
		ConvertToDig(placa)

try:
	mgmt()
except:
	pass