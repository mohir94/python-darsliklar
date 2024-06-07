# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:08:42 2024

@author: User
"""

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang 
# va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring
# Agar ro'yxatda bunday login mavjud bo'lsa, 
# "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanucchilar=['anvar', 'islom', 'mahmud', 'ozod', 'davron']
login=input("yangi login kiriting>>>>>>  ")
if login.lower() in foydalanucchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz, foydalanuvchi!")
    