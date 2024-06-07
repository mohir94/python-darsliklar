# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:21:02 2024

@author: User
"""

yosh=int(input('Yoshingiz nechida:  '))
if yosh<=4 or yosh>=60:
    print('Sizga kirish bepul')
elif yosh<18:
    print("kirish narxi 10000 so'm")
elif yosh>18:
    print("Kirish narxi 20000 so'm")