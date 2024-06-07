# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:00:07 2024

@author: User
"""
#  foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan 
#  va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan 
#  ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan 
#  ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "
#  Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, 
#  aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.


mahsulot=['anor','anjir','shaftoli' 'gilos', 'tarvuz', 'qovun', 'uzum','olma', 'banan','apelsin','kivi']
savat=[]
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing   '))
bor_mahsulotlar=[]
mavjud_emas=[]
for tovar in savat:
    if tovar in mahsulot:
        bor_mahsulotlar.append(tovar)
    else:
        mavjud_emas.append(tovar)
if mavjud_emas:
    print("Do'konimizda quyidagi tovarlar yo'q ")
    for tovar in mavjud_emas:
        print(tovar)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")