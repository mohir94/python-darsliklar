# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#                          5-DARS
#Kocha='Tepa'
#Mahalla='maydon'
#tuman='pop'
#print(f'{Kocha} kochasi,{Mahalla} mahallasi,{tuman} tuman,{viloyat} viloyati')
#Kocha=input("Qaysi ko'chada yashiysiz:   " )
#Mahalla=input("qaysi mahalla    ")
#tuman=input("qaysi tuman    ")
#viloyat=input("qaysi viloyat    ")
#print(f'{Kocha} kochasi,\n{Mahalla} mahallasi,\n{tuman} tuman,\n{viloyat} viloyati')
#manzil=f'{Kocha} kochasi, {Mahalla} mahallasi, {tuman} tumani,{viloyat} viloyati'
#print(manzil.upper())
#print(manzil.title())
#print(manzil.lower())


#                        6-DARS
#                       1-amaliyot
#son=int(input('Istalgan son kiriing \n>>>>>> '))
#print(f'{son} sonning kvadrati, {son**2} ga teng')
#print(f'{son} sonnin kubi {son**3} ga teng')

#                       2-amaliyot
#yosh=int(input("yoshingizni kiriting   >>  "))
#tug_yil=2024-yosh
#print("Siz", tug_yil, 'yilda tugilgansiz')


#                       3-amaliyot
#bir=float(input('Birinchi sonno kiriting >>>>>  '))
#ikki=float(input('Ikkinchi sonni kiriting >>>>  '))
#print(f'{bir} + {ikki} = {bir+ikki}')
#print(f'{bir} - {ikki} = {bir-ikki}')
#print(f'{bir} * {ikki} = {bir*ikki}')
#print(f'{bir} / {ikki} = {bir/ikki}')

#                          7-DARS
#                       1-amaliyot
#ismlar=['Kozim', 'Asad', 'Ahad']

#                       2-amaliyot
#print('salom', ismlar[0], 'bugun choyxonaga boramizmi',  ismlar[2], 'bilan', ismlar[1],'ham borar ekan')

#                       3-amaliyot
#sonlar=[2,10,-8,-6,14.5,23.1]

#                       4-amaliyot
#print(sonlar[0]+sonlar[-1])
#print(sonlar[3]+sonlar[4])
#print(sonlar[2]+sonlar[1])
#sonlar[-1]=25
#sonlar[2]=-8+10
#sonlar[0]=10+10

#                       5-amaliyot
#t_shaxslar=['Sino', "Buxoriy", 'Xorazmiy']
#z_shaxslar=['Ronaldu', 'Messi', 'Zidan']

#                       6-amaliyot
#print(f'Men tarixiy shaxslardan {t_shaxslar[0]} va {t_shaxslar[2]} , \nZamonaviy shaxslardan {z_shaxslar[0]} lar bilan suhbatlashishni xoxlar edim')

#                       7-amaliyot
#friends=[]
#friends.append('Abdu')
#friends.append('Ikrom')
#friends.append('Vali')
#friends.append('Zuhri')
#friends.append('Shox')

#                       8-amaliyot
#friends.remove('Shox')
#friends.remove('Ikrom')

#                       9-amaliyot
#friends.append('Qobil')
#friends.insert(0, 'Abdurahmon')
#friends.insert(2, 'Idris')

#                       10-amaliyot
#mehmonlar=[]
#mehmonlar.append(friends.pop(0))
#mehmonlar.append(friends.pop(3))
#print('kelgan mehmonlar:   ', mehmonlar)
#tuman='Mirobod'
#viloyat='Toshkent'
#Kocha='Fargona yoli'
#mahalla='Oltin kol'

#                          8-DARS
#                       1-amaliyot
davlatlar=['russia', 'spania','usa','eron','misr']

#                       2-amaliyot
#print('royxat uzunligi:  ', len(davlatlar))

#                       3-amaliyot
#print(sorted(davlatlar))

#                       4-amaliyot
#print(sorted(davlatlar, reverse=True))

#                       5-amaliyot
#print("Asl ro'yxat: ", davlatlar)

#                       6-amaliyot
#davlatlar.reverse()
#print(davlatlar)

#                       7-amaliyot
#davlatlar.sort()
#print("alifbo bo'yicha:  ", davlatlar)
#davlatlar.sort(reverse=True)
#print("alifboga teskari:  ", davlatlar)

#                       8-amaliyot
juft=list(range(120,1200,2))

#                       9-amaliyot
#print(sum(juft))

#                       10-amaliyot
#print(max(juft)-min(juft))

#                       11-amaliyot
#print(len(juft))

#                       12-amaliyot
#print(juft[:20])
#print(juft[260:280])
#print(juft[-20:])

#                       13-amaliyot
taomlar=['osh','mastava','shashlik', 'xonim', 'somsa']

#                       14-amaliyot
nonushta=taomlar[:]

#                       15-amaliyot
nonushta.remove('xonim')
nonushta.remove('shashlik')
nonushta.append('tuxum va sosika')
nonushta.append('kasha')

#                       16-amaliyot
#print('Nonushta menyusi:  ', nonushta)
#print('tushlik menyusi:   ', taomlar)

#                       16-amaliyot
#nonushta=tuple(nonushta)
#nonushta[0]='non va qaymoq'


#                          9-DARS
#                       1-2-amaliyot
#ismlar=['komol','bobur','oybek','umid','mohir']
#for ism in ismlar:
#    print(ism,'yaxshimisan')
#print('Kod', len(ismlar),'marta takrorlandi')

#                       3-amaliyot
#toq=list(range(11,100,2))
#for a in toq:
#    print(a**3)

#                       4-amaliyot
#kinolar=[]
#print("5 ta eng sevimli kinoni kiriting.")
#for n in range(5):
#    kinolar.append(input(f'{n+1}-kinoni kiriting:  '))
#print(kinolar)

#                       5-amaliyot
#odamlar=[]
#odam=int(input('bugun nechta odam bilan korishdingiz:  '))
#for o in range(odam):
#    odamlar.append(input(f'{o+1}- odam kim edi  '))
#print(odamlar)

#                          10-DARS
#                       1-amaliyot
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car=='gm':
#        print(car.upper())
#    else:
#        print(car.title())
        
#                       2-amaliyot
#for car in cars:
 #   if car!='gm':
 #       print(car.title())
#    else:
 #       print(car.upper())
 
#                       3-amaliyot
#login=input('loginni kiriting:  ')
#if login.lower()=='admin':
 #   print('Xush kelibsiz', login.title())
 #   print('Foydalanuvchilarni korishni boshlaymizmi')
#else:
 #   print('Xush kelibsiz foydalanuvchi', login.title())

#                       4-amaliyot
#print('Iltimos 2 ta son kiriting')
#a=float(input('Birinchi sonni kiriting:  '))
#b=float(input('Ikkinchi sonni kiriting:   '))
#if a==b:
 #   print(('<<<<<<< Sonlar teng >>>>>>').upper())
#else:
#    print(('<<<<<<< Sonlar teng emas >>>>>>>').upper())
    
#                       5-amaliyot    
#print('ISTALGAN SON KIRITING:  ')
#a=float(input('sonni kiriting    '))
#if a<0:
#    print("Manfiy son")
#else:
#    print("Musbat son")

#                       6-amaliyot  
print('ISTALGAN SON KIRITING:  ')
x=float(input("sonni kiriting:   "))
if x>0:
    print(f'{x}sonning ildizi {x**(1/2)} ga teng')
else:
    print("Manfiy son kiritdingiz")