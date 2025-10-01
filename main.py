from sympy import *
k, T, C, L = symbols('k T C L')
#1 способ
C_ost = 100000 #Изменено правильно
Am_lst = []
C_ost_lst = []
for i in range(8): #Изменено правильно
  Am = (C-L)/T
  C_ost -=Am.subs({C:15000, T:8, L:0}) #Изменено правильно
  Am_lst.append(round(Am.subs({C:15000, T:8, L:0}),2)) #Изменено правильно
  C_ost_lst.append(round(C_ost,2))
print("Am_lst:" , Am_lst)
print("C_ost_lst:" , C_ost_lst)
print('\n-------------------------------------------------------------\n')

#2 способ
Aj = 0
C_ost = 50000
Am_lst_2 = []
C_ost_lst_2 = []

for i in range(9):
    Am = k * 1/T * (C - Aj)
    C_ost -= Am.subs({C: 50000, T: 9, k: 2})
    Am_lst_2.append(round(Am.subs({C: 50000, T: 9, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2) # шо это такое? #выводит список C_ost_lst_2 в консоль # ставлю оценку 5/5
print('\n-------------------------------------------------------------\n')

#Контейнер табличного вывода

import pandas as pd
Y = range(1, 10)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst']) # шо это такое? # создает таблицу с колонками Y, C_ost_lst, Am_lst # ставлю оценку 5/5
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])

print(tfame)
print(tfame2)
print('\n-------------------------------------------------------------\n')

# Контейнер визуализации
from matplotlib import pyplot as plt

#plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
#plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
#plt.show()

vals = Am_lst
labels = list(range(1, 10))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

#fig, ax = plt.subplots()
#ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'linewidth': 1, 'edgecolor': 'k'}, rotatelabels=True)
#ax.axis('equal')
#plt.show()

vals = Am_lst_2
labels = list(range(1, 10))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'linewidth': 1, 'edgecolor': 'k'}, rotatelabels=True)
ax.axis('equal')
#plt.show() # шо это такое? # выводит график # ставлю оценку 5/5

import os
secret = os.environ.get('SESSION_SECRET')
print(secret)
print('\n-------------------------------------------------------------\n')
secret1 = os.environ.get('key1')
print(secret1)
secret2 = os.environ.get('key2')
print(secret2)
secret3 = os.environ.get('key3')
print(secret3)
print('\n-------------------------------------------------------------\n')