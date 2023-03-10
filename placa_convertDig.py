import pandas as pd
import re
import os

class ConvertToDig:
	def __init__(self, placa):
		self.placa = placa
		i = str(placa[4])
		
		alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		
		new_placa = f'{placa[:4]}{alph.index(i)}{placa[5:7]}'.upper()
		df = pd.DataFrame({0: [new_placa]})
		df.to_clipboard(index=False, header=False)
		
		print()
		print('Placa '+new_placa+' copiada!')
		os.system('pause')