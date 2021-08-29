# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 01:09:55 2021

@author: adamkritz
"""

import pandas as pd

#enter the csv for your collection from ygoprodeck.com
yug1 = pd.read_csv('')

yug=yug1.copy()

del yug['cardrarity']
del yug['cardcondition']
del yug['card_edition']
del yug['cardset']
del yug['cardcode']

count1 = len(yug)
z=0

while z < count1:
    if yug['cardq'][z] >3:
        yug['cardq'][z]=3
        z= z+1
    else:
        z=z+1
y = []

yug['Counts'] = yug.groupby(['cardname'])['cardid'].transform('count')

count1 = len(yug)
z=0
while z < count1:  
    if yug['Counts'][z] >3:
        g = '{} 3 --{}'.format(yug['cardid'][z], yug['cardname'][z])
        y.append(g)
        z= z+1
    else:
        z=z+1

y = list(set(y))

stop = {'cardname':'Stopper', 'cardq':'Stopper', 'cardid':'Stopper', 'Counts': 0}
yug = yug.append(stop, ignore_index=True)

count = len(yug)
x=0

while x < count:   
    if (yug['Counts'][x]== 2):
        s = int(yug['cardq'][x])+ int(yug['cardq'][x+1])
        if s >3:
            s=3
        m = '{} {} --{}'.format(yug['cardid'][x], s, yug['cardname'][x])
        y.append(m)
        s=0
        x = x+2
    if (yug['Counts'][x]== 3):
        f = '{} 3 --{}'.format(yug['cardid'][x], yug['cardname'][x])
        y.append(f)
        x = x+3
    if (yug['Counts'][x]==1):
        w = '{} {} --{}'.format(yug['cardid'][x], yug['cardq'][x], yug['cardname'][x])  
        y.append(w)
        x = x+1
    if (yug['Counts'][x]>3) or (yug['Counts'][x]==0) :
        x = x+1
        
for x in y:
    if (x != 'Stopper 3 --Stopper') and (x != 'Stopper Stopper --Stopper'):
        print(x)
        
        
# copy this output into a banlist (.conf file)
pd.set_option('display.max_rows', 500)
 





