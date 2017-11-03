import re
import pandas as pd
import numpy as np
import csv



f = open('chat.txt', 'r',encoding="utf8")
s=f.readlines()
rows = []
extrarows=[]
extrarec=[]
#print(s[1:100])
for line in s:
   if line[0:1].isdigit()==True: # added this to remove unexpected \n\ns in message texts 
           row=line.split(":")
           if len(row)>=5:
               row1= ':'.join(row[0:3]) ,''.join(row[3]),''.join(row[4:])
               rows.append(row1)
           else:
                extrarows.append(row) # subjectchanges
   else:
           extrarec.append(line)
#print(extrarows[1:10])
#print(extrarec[1:10])
df= pd.DataFrame(rows,columns =['DateTime','sender','text'])
df['Datecolum']=pd.to_datetime(df['DateTime'])
df['spliwords']=df['text'].str.split()
print (df[:10])