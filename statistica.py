import dill, os, pickle
import pandas as pd
from tkinter.simpledialog import askstring
user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)
filename = askstring('Entry', 'Inserisci il nome del file csv con i dati (senza estensione)')
#print('Your dataframe will be named <df>')
df = pd.read_csv('%s.csv' % filename)
print('Questa è la struttura dei tuoi dati:')
print(df.info())
column_name = askstring('Entry', 'Inserisci il nome della colonna che ti interessa') 
DATA = df['%s' % column_name]
DATA_ls = DATA.to_list()
COUNT = len(DATA_ls)

def maxarray(dataframe):
	M = dataframe[0]
	for i in dataframe:
		if i > M:
			M = i
	return M
MAX = maxarray(DATA)

def minarray(dataframe):
	m = dataframe[0]
	for i in dataframe:
		if i < m:
			m = i
	return m
MIN = minarray(DATA)

SUM = 0
for i in range(len(DATA_ls)):
	SUM = SUM + DATA_ls[i]
AVERAGE = SUM / len(DATA_ls)

VARIANCE = 0
for i in range(len(DATA_ls)):
	VARIANCE = VARIANCE + (DATA_ls[i] - AVERAGE)**2
VARIANCE = VARIANCE / (len(DATA_ls)-1)

print('La taglia del campione su cui è stata misurata la variabile <%s> è %d' % (column_name, COUNT))
if column_name == 'peso_corporeo_g':
	print('Il valore massimo della variabile <%s> è %f grammi' % (column_name, MAX))
	print('Il valore minimo della variabile <%s> è %f grammi' % (column_name, MIN))
	print('La media della variabile <%s> è %f grammi' % (column_name, AVERAGE))
	print('La varianza della variabile <%s> è %f grammi^2' % (column_name, VARIANCE))
else:
	print('Il valore massimo della variabile <%s> è %f Watt' % (column_name, MAX))
	print('Il valore minimo della variabile <%s> è %f Watt' % (column_name, MIN))
	print('La media della variabile <%s> è %f Watt' % (column_name, AVERAGE))
	print('La varianza della variabile <%s> è %f Watt^2' % (column_name, VARIANCE))
