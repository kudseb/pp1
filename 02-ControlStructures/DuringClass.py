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
"""
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