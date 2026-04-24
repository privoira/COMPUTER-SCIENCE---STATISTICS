import os
import pandas as pd
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askfloat
user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)

frequenze_AA=[]
frequenze_Aa=[]

p=[]
AA=[]
Aa=[]

p_iniziale=[]
q_iniziale=[]
risultato_AA=[]
risultato_aa=[]
risultato_Aa=[]

n = askinteger('Entry', 'Inserisci il numero di generazioni')
Aa_start = askfloat('Entry', 'Inserisci la frequenza iniziale degli ETEROZIGOTI')

#CALCOLO LE FREQUENZE INIZIALI (PRIMA DELLA SELEZIONE)
risultato_Aa.append(Aa_start)
Aa.append(Aa_start)
p_iniziale.append((2+(4-4*2*risultato_Aa[0])**0.5)/4)
q_iniziale.append(1-p_iniziale[0])
AA=p_iniziale[0]**2
risultato_AA.append(AA)
print("Frequenza iniziale di AA")
print(risultato_AA[0])
print("Frequenza iniziale di Aa")
print(risultato_Aa[0])


for i in range(n):

    risultato_AA=risultato_AA[i]/(risultato_AA[i]+risultato_Aa[i])
    frequenze_AA.append(risultato_AA)
    
    risultato_Aa=(1-risultato_AA)/(risultato_AA+(1-risultato_AA))
    frequenze_Aa.append(risultato_Aa)
        
    frequenze_Aa.append(frequenze_AA[i]*frequenze_Aa[i]+(frequenze_Aa[i]**2)/2)
    frequenze_AA.append(frequenze_AA[i]**2+frequenze_AA[i]*frequenze_Aa[i]+(frequenze_Aa[i]**2)/4)
    
    risultato_Aa=frequenze_Aa
    risultato_AA=frequenze_AA

df1 = pd.DataFrame(frequenze_AA).T
df2 = pd.DataFrame(frequenze_Aa).T
frames = [df1, df2]
result = pd.concat(frames)

result.to_excel(excel_writer='dati_%d_generazioni.xlsx' % n)
dataframe = pd.read_excel('dati_%d_generazioni.xlsx' % n)
print('FREQUENZE FENOTIPICHE CON %d GENERAZIONI' % n)
print(dataframe.head())
print('Prima riga: frequenze degli OMOZIGOTI AA')
print('Seconda riga: frequenze degli ETEROZIGOTI Aa')
