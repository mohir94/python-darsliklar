# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:19:32 2024

@author: User
"""

# Foydalanuvchidan biror butun son kiritishni so'rang. 
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini
# konsolga chiqaring. 

son=int(input('Butun son kiriting:   '))
for n in range(2,11):
    if not (son%n):
        print(f'{son} soni {n} ga qoldiqsiz bo\'linadi')