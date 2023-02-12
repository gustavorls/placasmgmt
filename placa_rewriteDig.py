import pandas as pd
import re
import os

class RewriteDig:
	def __init__(self, placa):
		self.placa = placa
		df = pd.DataFrame()
		c = int(input("Digite a posição do caractere necessário: "))
		
		for i in range(10):
			new_placa = f'{placa[:c-1]}{i}{placa[c:7]}'.upper()
			df1 = pd.DataFrame({0: [new_placa]})	
			df = pd.concat([df, df1])
		
		df.to_clipboard(index=False, header=False)
		
		print(re.sub("Pl","\nPl","Placas copiadas!"))
		os.system('pause')