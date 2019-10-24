import random
#25
'''
for i in range(3):
    for j in range(7):
        print('*',end='')
    print()

#26
for i in range(1,10):
    for j in range(1,i+1):
        print(i,end='')
    print()

#27
n=9
for i in range(1,n//2+2):
    for j in range(1,i+1):
        print('*',end='')
    print()
for k in range(n//2,0,-1):
    for j in range(1,k+1):
        print('*',end='')
    print()

#z28
a28=4
b28=15
for j in range(1,b28+1):
    print('*',end='')
print()
for i in range(2,a28):
    print('*',end='')
    for j in range(2,b28):
        print(' ',end='')
    print('*')
for j in range(1,b28+1):
    print('*',end='')
print()

#29
tab29=[15,8,31,47,2,19]
print ('tab: ',end='')
for i in tab29:
    print(i,'',end='')
print ()
print ('tab reverse: ',end='')
for i in range(len(tab29)-1,-1,-1):
    print(tab29[i],'',end='')
print ()

#30
pin30 = '0850'
zle = 0
while zle <3:
    print('Podaj kod pin: ')
    x=input()
    if x == pin30:
        print('Pin ok')
        break
    else:
        print('Kod pin niepoprawny')
        zle+=1
else:
    print('Karta zablokowana')

#31
uczelnia='Uniwersytet Ekonomiczny w Krakowie'
print(uczelnia)
print('Szeroko: ',end='')
for i in uczelnia:
    print(i,'',end='')

#32
print ('Podaj ciag znakow: ')
x32=input()
for i in range(len(x32)-1,-1,-1):
    print(x32[i],end='')

#33
print('Podaj liczbe: ')
x33=input()
tab33=['zero','jeden','dwa','trzy','cztery','piec','szesc','siedem','osiem','dziewiec']
print(f'{x33} - ')
for i in x33:
    print(tab33[int(i)],'',end='')
#34
rok='2018'
print('Podaj pesel')
pesel=input()
print('Plec: Kobieta') if int(pesel[10])%2 ==0 else print('Plec: mezczyzna')
rocznik=int(pesel[0:2])
wiek=int(rok[2:4])
print(f'Wiek:{(100-rocznik)+wiek}') if rocznik>=wiek else print(f'Wiek:{wiek-rocznik}')

#35
print('Podaj a: ')
a=int(input())
print('Podaj b: ')
b=int(input())
print('Podaj c: ')
c=int(input())
delta=(b**2)-(4*a*c)
if delta>0:
    print(f'dwa pierwiastki: x1={round((-b-(delta**(1/2)))/(2*a),2)}, x2={round((-b+(delta**(1/2)))/(2*a),2)}')
elif delta<0:
    print('nie ma pierwiastkow')
else:
    print(f'jeden pierwiastek: x1={round(-b/(2*a),2)}')
    
#36
i=1;
while True:
    if i%7==0 and i%2==1 and i%3 ==1 and i%4 ==1 and  i%5 ==1 and i%6 ==1:
        print('Liczba z zad36: ',i)
        break
    else:
        i+=1
        
#37
licz37=[15,26,29,40]
for i in range(0,len(licz37)-1):
    if licz37[i]>licz37[i+1]:
        a=licz37[i+1]
        licz37[i+1]=licz37[i]
        licz37[i]=a
if len(licz37)%2==0:
    median=(licz37[(len(licz37)//2)-1]+licz37[len(licz37)//2])/2
    print (median)
else:
    print(licz37[(len(licz37)//2)])

#38
i=7
j=0
while i >=0:
    while j<3:
        print(i+j,end=' ')
        j+=1
    i-=3
    j=0
    print()

#39
p1=0
p2=1
print(p1,p2,end=' ')
for i in range(24):
    p1=p1+p2
    print(p1,end=' ')
    p2=p1+p2
    print(p2,end=' ')

#40
rzuty=[['jedynka',0],['dwojka',0],['trojka',0],['czworka',0],['piatka',0],['szostka',0]]
for i in range(100):
    kostka=random.randint(1,6)
    if kostka ==1:
        rzuty[0][1]+=1
    elif kostka ==2:
        rzuty[1][1]+=1
    elif kostka ==3:
        rzuty[2][1]+=1
    elif kostka ==4:
        rzuty[3][1]+=1
    elif kostka ==5:
        rzuty[4][1]+=1
    elif kostka ==6:
        rzuty[5][1]+=1
for i in range(0,6):
    print(rzuty[i][0],':',rzuty[i][1])

#41
tab41=[]
while True:
    print('Podaj liczbę: ')
    x=int(input())
    if x==0:
        break
    else:
        tab41.append(x)
suma=0
for i in tab41:
    suma+=i
print(f'Rezultat: Liczb={len(tab41)}, Suma={suma}, średnia={suma/len(tab41)}')

#42
print('Podaj liczbe dzielona')
x42=int(input())
print('Podaj dzielnik')
y42=int(input())
print('Dzielenie przez 0') if y42 ==0 else print(x42/y42)

#43
tab43=[]
for i in range(1,4):
    print(f'Podaj {i} liczbę : ')
    tab43.append(int(input()))
tab43.sort()            
print('Liczby w kolejnosci rosnacej: ',tab43)

#44
print('Podaj limit predkosci(km/h) : ')
x44=int(input())
print('Podaj predkosc pojazdu(km/h) : ')
y44=int(input())
roznica44=y44-x44
if roznica44 <10 and roznica44 >0:
    print(f'Mandat (zl) : {roznica44*5} ')
else:
    mandat=10*5
    roznica44-=10
    mandat+=roznica44*15
    print(f'Mandat (zl) : {mandat} ')

#45
print('ile liczb pierwszych: ')
n44=int(input())
pierw44=[]
i44=2
while len(pierw44)<n44-1:
    jest=False
    for x in pierw44:
        if i44%x==0:
            jest=True
            break
    if not jest:
        pierw44.append(i44)
    i44+=1
pierw44.insert(0,1)
print(pierw44)

#46
tab45=[]
for i in range(0,21):
    tab45.append(random.randint(-20,-5))
print(tab45)
#47
print('Podaj kwote w zl: ')
x47=int(input())
print(f'5zl: {x47//5}')
print(f'2zl: {(x47%5)//2}')
print(f'1zl: {((x47%5)%2)//1}')

#48
for i in range(1,8):
    for j in range(1,8):
        print(f'{i*j} ','',end='')
    print()

#49
nrdniatygodnia=2
print("| PN | WT | SR | CZ | PT | SB | ND |")
print('|',end='')
i=0    
while nrdniatygodnia>0:
    print('    |',end='')
    nrdniatygodnia-=1
    i+=1
for j in range(1,31):
    print(f' {j} |',end='')
    i+=1
    if i%7==0:
        print()
        print('|',end='')
        i=0

#50
print('Podaj wartosc do zamiany na binarny')
x50=int(input())
wynik=[]
while x50>0:
    r=x50%2
    wynik.insert(0,r)
    x50=x50//2
print(f'= {wynik} (2)')
'''