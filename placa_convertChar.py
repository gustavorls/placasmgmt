import pandas as pd
import re
import os

class ConvertToChar:
	def __init__(self, placa):
		self.placa = placa
		i = int(placa[4])
		
		alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		
		new_placa = f'{placa[:4]}{alph[i]}{placa[5:7]}'.upper()
		df = pd.DataFrame({0: [new_placa]})
		df.to_clipboard(index=False, header=False)
		
		print()
		print('Placa '+new_placa+' copiada!')
		os.system('pause')