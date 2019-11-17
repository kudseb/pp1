import random
import copy
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

#28
nazwy=['java','python','js','c++','c#','ruby','perl','php','c','android']
val=[61,47,37,32,26,18,14,14,9,7]
def rysujWykres(jezyki,wartosci):
    for i in range(0,len(jezyki)):
        print(f'{jezyki[i]} : ',end='')
        x=val[i]
        while x>2:
            print('#',end='')
            x-=2
        print()
rysujWykres(nazwy,val)

#29
tab29=[2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]
def mediana(tab):
    tab.sort()
    y=len(tab)//2
    if len(tab)%2==0:
        return tab[y]+tab[y+1]
    else:
        return tab[y]
def dominanta(tab):
    tabczest=[[tab[0],0]]
    for i in tab:
        powtarz=False
        for j in range(0,len(tabczest)):
            if i==tabczest[j][0]:
                tabczest[j][1]+=1
                powtarz=True
                break
        if powtarz==False:
            tabczest.append([i,1])
    najw=0
    for i in range(len(tabczest)-1):
        if tabczest[i-1][1]>tabczest[i][1]:
            najw=tabczest[i-1][0]
        else:
            najw=tabczest[i][0]
    return najw
print(dominanta(tab29))
print(mediana(tab29))

#30
def los():
    return random.randint(1,50)
parz=0
nieparz=0
for i in range(1000):
    x=los()
    if x%2==0:
        parz+=1
    else:
        nieparz+=1
print(f'Liczby parzyste {round(parz/10,2)}%')
print(f'Liczby nieparzyste {round(nieparz/10,2)}%')

#31
def reverse(tab):
    tab2b=[]
    i=len(tab)-1
    while i>=0:
        tab2b.append(tab[i])
        i-=1
    return tab2b
tab=[2,5,4,1,8,7,0,9]
print(reverse(tab))

#32
def transpozycja(macierz):
    macierz2b = copy.deepcopy(macierz)
    for i in range(0,len(macierz)):    
        for j in range(0,len(macierz[i])):
            macierz2b[j][i]=macierz[i][j]
    return macierz2b
macierz=[[1,2,0],
         [0,0,3],
         [5,1,1]]
print(macierz)
print(transpozycja(macierz))

#33
def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        print(a)
fib(20)
#34
#moze mozna dodac print do return i wtedy nie trzeba petli
def fibi(n):
    if n==0 or n==1:
        return 1;
    else:
        return fibi(n-1)+fibi(n-2)
for i in range(20):
    print(fibi(i))

#35

def z35(n):
    if n//10==0:
        return n
    else:
        return n%10+z35(n//10)
print(z35(12345589))

#36 no idea
'''
tab=[7,5,[3,6,[2]],7,[1,[2,3,[4]],9,2],4]
def z36(tab):
    if isinstance(tab,int):
        return tab
    else:
        if isinstance(tab[0],int):
            return tab.pop(0)+z36(tab)
        else:
            suma=0
            for i in range(0,len(tab[0])):
                if isinstance(tab[0][i],int):
                  suma+=tab[0][i]
                else:
                    z36[tab[0].pop(i)]
            return suma
tab22=[2,3,1,[1,2,3]]
z36(tab)
'''
#37 #mozna by bylo posortowac tablice i sprawdzic czy po lewej i prwaej nie ma takich samych wartosci
def z37(tab):
    tab2=[]
    for i in range(0,len(tab)):
        powtarz=False
        for j in range(0,len(tab)):
            if i==j:
                pass
            else:
                if tab[i]==tab[j]:
                    powtarz=True
        if powtarz==False:
            tab2.append(tab[i])
    return tab2
print(z37([2,5,7,2,5,7,1,1,2,8,9,100,90]))

#38
def z38(s):
    res=''
    for i in s:
        if ord(i) >=65 and ord(i)<=90:
            res+=(i)
    return res
print(z38('Ala ma kota,Darek Maciborek, Kapitan Gwiezdenej Floty'))

#39
def z39(n,x,y):
    if y<x:
        x,y=y,x
    if n>=x and n<=y:
        return 'miesci sie'
    else:
        return 'nie miesci sie'
print(z39(10,10,3))

#40
lam=lambda x : not(x%2)
tab=[1,2,3,4,5,6,7,8]
x=filter(lam,tab)
for i in x:
    print(i)
'''