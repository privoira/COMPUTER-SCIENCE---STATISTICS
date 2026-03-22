import os
import pandas as pd
from tkinter.simpledialog import askinteger
user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)
from tartaglia_triangolo_modulo import triangolo
n = askinteger('Entry', 'Inserisci il numero di loci')

frequenze_fenotipiche_assolute=triangolo[n+1]

freq=[]
frequenze_fenotipiche_relative=[]

for i in range(len(frequenze_fenotipiche_assolute)):
    result = frequenze_fenotipiche_assolute[i]/sum(frequenze_fenotipiche_assolute)
    freq.append(result)

for i in range(len(frequenze_fenotipiche_assolute)):
    result = frequenze_fenotipiche_assolute[i]/sum(frequenze_fenotipiche_assolute)
    frequenze_fenotipiche_relative.append(result)

#print(frequenze_fenotipiche_relative)
result = []
for i in range(len(freq)-1):
    freq[i+1]=freq[i]+freq[i+1]
    result.append(freq[i+1])

#for i in range(len(freq)):
#    print('Il vettore delle frequenze cumulative è %f' % freq[i])

frequenze_fenotipiche_cumulative=freq
df1 = pd.DataFrame(freq).T
df1 = pd.DataFrame(frequenze_fenotipiche_assolute).T
df2 = pd.DataFrame(frequenze_fenotipiche_relative).T
df3 = pd.DataFrame(frequenze_fenotipiche_cumulative).T

frames = [df1, df2, df3]
result = pd.concat(frames)
result.to_excel(excel_writer='dati_%d_loci.xlsx' % n)
dataframe = pd.read_excel('dati_%d_loci.xlsx' % n)
print('FREQUENZE FENOTIPICHE CON %d LOCI' % n)
print(dataframe.head())
print('Prima riga: frequenze fenotipiche assolute')
print('Seconda riga: frequenze fenotipiche relative')
print('Terza riga: frequenze fenotipiche cumulative')
