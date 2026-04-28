import os
import pandas as pd
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askfloat
user = os.getlogin()
os.chdir('/home/%s/COMPUTER_SCIENCE/AI' % user)

AA=[]
Aa=[]
aa=[]
risposta_alla_selezione=[]

n = askinteger('Entry', 'Inserisci il numero di generazioni')
Aa_start = askfloat('Entry', 'Inserisci la frequenza iniziale degli ETEROZIGOTI')
Aa.append(Aa_start)
# Aa_start è il primo elemento del vettore <Aa> 

# calcolo la frequenza iniziale p dell'allele A
# 2*p*(1-p)=Aa_start
# x = (2+(4-4*2*Aa_start)**0.5)/4

delta = 4-4*2*Aa[0]

if delta > 0:
    p_start = (2+delta**0.5)/4
else:
    p_start = (2+(delta*(-1))**0.5)/4
    
AA.append(p_start**2)
# calcolo la frequenza iniziale degli omozigoti dominanti [Freq(AA) = F9)] e la assegno, come primo elemento, al vettore AA

AA.append(AA[0]/(AA[0]+Aa[0]))
Aa.append(Aa[0]/(AA[0]+Aa[0]))
#AA
#[0.25, 0.3333333333333333]
#Aa
#[0.5, 0.6666666666666666]

# calcolo la frequenza degli omozigoti dominanti (AA = B11) dopo la prima generazione di selezione: Freq(AA) = AA[1]
# calcolo la frequenza degli eterozigoti [Freq(Aa) = C11] dopo la prima generazione di selezione: Freq(Aa) = Aa[1] 

for i in range(1, n):

    AA.append((AA[i]**2+AA[i]*Aa[i]+(Aa[i]**2)/4)/((AA[i]**2+AA[i]*Aa[i]+(Aa[i]**2)/4)+(AA[i]*Aa[i]+(Aa[i]**2)/2)))
    Aa.append((AA[i]*Aa[i]+(Aa[i]**2)/2)/((AA[i]**2+AA[i]*Aa[i]+(Aa[i]**2)/4)+(AA[i]*Aa[i]+(Aa[i]**2)/2)))


aa.append((1-p_start)**2)
# calcolo la frequenza iniziale degli omozigoti recessivi aa 

for i in range(1, n):
    aa.append(((Aa[i])**2)/4)
# calcolo la frequenza degli omozigoti recessivi aa

for i in range(1, n):
    risposta_alla_selezione.append(aa[i-1]-aa[i])
# calcolo la risposta alla selezione

df1 = pd.DataFrame(AA).T
df2 = pd.DataFrame(Aa).T
df3 = pd.DataFrame(aa).T
df4 = pd.DataFrame(risposta_alla_selezione).T

frames = [df1, df2, df3, df4]
result = pd.concat(frames)

result.to_excel(excel_writer='dati_%d_generazioni.xlsx' % n)
dataframe = pd.read_excel('dati_%d_generazioni.xlsx' % n)
print('FREQUENZE FENOTIPICHE CON %d GENERAZIONI' % n)
print(dataframe.head())
print('Prima riga: frequenze degli OMOZIGOTI AA')
print('Seconda riga: frequenze degli ETEROZIGOTI Aa')
print('Terza riga: frequenze degli OMOZIGOTI aa')
print('Quarta riga: risposta alla selezione [Fn-1(aa)-Fn(aa)]')
