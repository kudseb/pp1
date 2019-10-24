"""
#8
x8=10
y8=9
print(f"{x8} jest wieksze") if x8>y8 else print(f"{y8} jest wieksze")
#9
x9=14
print(x9%2==0)
#10
x10=int(input())
if x10>0 and x10%2 == 1:
    print(f"{x10} jest dodatnia i nieparzysta")

#11
login11='marek'
haslo11='m-123'
print("Podaj login")
x11=input()
print("Podaj haslo")
y11=input()
if x11==login11 and y11==haslo11:
    print('Zalogowano')
else:
    print("Podane dane są nieprawidłowe")
#12
x12=int(input())
y12=int(input())
if x12<0 or y12<0:
    print(f"Ktoras z tych zmiennych jest ujemna: {x12} {y12}")
    

#13
print("Podaj 1 współrzedna")
x13=int(input())
print("Podaj 2 współrzedna")
y13=int(input())
if x13>0 and y13>0:
    print("Punkt {x13} {y13} znajduję sie w I ćwiartce")
elif x13<0 and y13>0:
    print("Punkt {x13} {y13} znajduję sie w II ćwiartce")
elif x13<0 and y13<0:
    print("Punkt {x13} {y13} znajduję sie w III ćwiartce")
elif x13>0 and y13<0:
    print("Punkt {x13} {y13} znajduję sie w IV ćwiartce")

#14
print("Podaj wiek psa w psich latach: ",end='')
x14=int(input())
wynik14=0
if x14>2:
    wynik14+=2*10.5
    x14-=2
    wynik14+=x14*4
else:
    wynik14+=x14*10.5
print(f"Wiek psa w psich latach to {round(wynik14)} lata")

#LOOOOOPSS
#15
x15=int(input())
#for i15 in range(1,11):
#    print(f"{x15} x {i15} = {x15*i15}")
i15=1
while i15<=10:
    print(f"{x15} x {i15} = {x15*i15}")
    i15+=1

#16
for i16 in range(1,11):
    print(f"1/{i16} = {1/i16}")

#17
sparz=0
snieparz=0
for i17 in range(1,51):
    if i17%2==0:
        sparz+=i17
    else:
        snieparz+=i17
print(f"Suma parzystych: {sparz} ,a nieparzystych : {snieparz}")

#18
for i18 in range(1,31):
    if i18%3==0 and i18%5==0:
       print("BINGO ", end='')
    elif i18%3 == 0:
        print("THREE ",end='') 
    elif i18%5 == 0:
        print("FIVE " , end='')
    else:       
        print(f"{i18} ",end='')

#19
print('podaj ile wyrazow ciagu wyswietlic : ')
n19=int(input())
wyrazciag=1
for i in range(n19):
    print(f'{i+1} wyraz ciagu = ',wyrazciag+i*3)


#22
tab22=[15,8,31,47,2,19]
n=0
sumtab22=0
for i in tab22:
    if i %2 == 1:
        sumtab22+=i
        n+=1
print(f"Srednia artymetyczna = {round(sumtab22/n,2)}")

#23
print("Podaj ocene od 1 do 6 : ")
x23=int(input())
tab23=['niedostateczny','mierny','dostateczny','dobry','bardzo dobry','celujacy']
print(f'Ocena slownie: {tab23[x23-1]}')
#24
tab24=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']
spam24=[0,0]
for i in tab24:
    x=len(i)
    if x>spam24[0]:
        spam24[0]=x
        spam24[1]=i
print(f'najdluzsze imie: {spam24[1]}')
"""