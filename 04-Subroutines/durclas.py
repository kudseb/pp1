#5
'''
def printName():
    print('Grzegorz Brzęczyszczykiewicz')
printName()

#6
def uek():
    print("Uniwersytet Ekonomiczny w Krakowie")
    print("ul. Rakowicka 27")
    print("31-510 Kraków")
uek()
uek()

#7
def zad7():
    for i in range(1,10):
        if i%3==0:
            print(f'{i} ',end='')
            print()
        else:
            print(f'{i} ',end='')
zad7()
#8
x=3
def f():
    x=1
f()
print(x)

#9
def f():
    s = "I love Disco Polo!"
    print(s)
s = "I love Rock & Roll!"
f()
print(s)

#10
def f():
    y = x + 2
    return x + y
x = 3
y = x + 4
z = f() + x + y
print(x, y, z)
#11

def f():
    x = y
    x[1] = y[0] + x[1]
x = [1,2,3]
y = [4,5]
f()
print(x,y)

#13
def suma(tab):
    print(tab)
    s=0
    for i in tab:
        if int(i)==i:
            s+=i
    return s
print(suma([4,3,7,1,3]))

#14
def wystepuje(tab,szuk):
    czywyst='nie występuje'
    for i in tab:
        if int(i) == szuk:
            czywyst='występuje'
            return czywyst
    return czywyst
print(f" Podana liczba {wystepuje([15,38,7,23,14],23)} w tablicy")

#17
import random
def rzucKostka():
    return random.randint(1,6)
suma=0
for i in range(3):
    x=rzucKostka()
    print(x,end=' ')
    suma+=x
print()
print(f"Suma oczek {suma}")

#18
def silnia(n):
    #0!=1 oraz 1!=1
    if n==0 or n==1:
        return 1
    #n! = n * (n-1)!
    if n > 1:
        return n * silnia(n-1)
print( f'5! = {silnia(5)}' )

#19
def suma(n):
    if n==1:
        return 1
    if n>1:
        return n+suma(n-1)
print(suma(500))

#20
def potega(x,n):
    if n==1:
        return x
    if n>1:
        return x*potega(x,n-1)
print(f'5 do potegi 3 : {potega(5,3)}')

#21
multiplication = lambda x,y: x*y
print( multiplication(3,4) )

#22
ay22=lambda x: not x%2
print(ay22(2))

#23
ay=lambda x,y: True if x>y else False
print (ay(5,2))

#24
def miesiac(n):
    tab=['styczeń','luty','marzec','kwiecień','maj','czerwiec','lipiec','sierpień','wrzesień','październik','listopad','grudzień']
    return tab[n-1]
print(miesiac(7))
print(miesiac(9))

#25
imiona= ['Janek', 'Ania', 'Wojtek', 'Zosia']
def jestimie(imie,imiona):
    czywyst='nie występuje'
    for i in imiona:
        if  i== imie:
            czywyst='występuje'
            return czywyst
    return czywyst
print(f"Imie {jestimie('Wojtek',imiona)}  w wykzie imion ")

#26
def podatek(dochod):
    if dochod<=5000:
        return int(dochod*0.17)
    elif dochod>5000:
        return int((5000*0.17)+(dochod-5000)*0.32)
    
print('Podatek nalezny: ',podatek(int(input('Podaj dochód: '))))

#27
#samog=['a','e','y','i','o','ą','ę','u','ó']
def ilsamwtesk(tekst='Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.',samog=['a','e','y','i','o','ą','ę','u','ó']):
    #samog=['a','e','y','i','o','ą','ę','u','ó']
    czest=[0,0,0,0,0,0,0,0,0]
    liczznak=0
    for i in tekst:
        for j in range(0,9):
            if i==samog[j]:
                czest[j]+=1
                liczznak+=1
    for i in range(0,9):
        czest[i]=round(czest[i]/liczznak,2)
    print(f'W tekscie skladajacym sie z {liczznak} znakow ,samogloski w %:')
    print(samog)
    print(czest)
ilsamwtesk()
'''
#28
nazwy=['java','python','js','c++','c#','ruby','perl','php','c','android']
val=[61,47,37,32,26,18,14,14,9,7]
def rysujWykres(jezyki,wartosci):
    for i in range(0,len(jezyki)):
        print(f'')
        
rysujWykres(nazwy,val)