# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:37:58 2024

@author: User
"""

mahsulot=['anor','anjir','shaftoli' 'gilos', 'tarvuz', 'qovun', 'uzum','olma', 'banan','apelsin','kivi']
savat=[]
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing   '))
for tovar in savat:
    if tovar in mahsulot:
        print(f'Do\'konimizda {tovar} bor')
    else:
        print(f'Do\'konimizda {tovar} yo\'q')