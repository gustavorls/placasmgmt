import pandas as pd
import re
import os

class RewriteChar:
	def __init__(self, placa):
		self.placa = placa
		df = pd.DataFrame()
		c = int(input("Digite a posição do caractere necessário: "))
		
		i = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		
		for j in range(len(i)):
			new_placa = f'{placa[:c-1]}{i[j]}{placa[c:]}'.upper()
			df1 = pd.DataFrame({0: [new_placa]})	
			df = pd.concat([df, df1])
		
		df.to_clipboard(index=False, header=False)
		print(re.sub("Pl","\nPl","Placas copiadas!"))
		os.system('pause')