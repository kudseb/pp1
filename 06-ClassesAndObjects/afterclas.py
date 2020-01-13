import math
import random
import copy
'''
#17
class ulamek():
    def __init__(s,licz,mian):
        s.licznik=licz
        if mian == 0:
            raise Exception('Tylko mianownik rozny od zera')
        else:
            s.mianownik=mian
    def wysw(s):
        print(f'{s.licznik}/{s.mianownik}')
    def uprosc(s):
        x=math.gcd(s.licznik,s.mianownik)
        s.licznik//=x
        s.mianownik//=x
x=ulamek(1,2)
x.wysw()
x.uprosc()
x.wysw()
print()
y=ulamek(12,21)
y.wysw()
y.uprosc()
y.wysw()

#18
class kostka():
    def __init__(s):
        s.oczka=0;
        pass
    def rzuc(s):
        x=random.randint(1,6)
        s.oczka=x
        return x
tab18=[]
for i in range(3):
    tab18.append(kostka())
suma=0
for i in tab18:
    x=i.rzuc()
    suma+=x
    print(x)
print(suma)

#19
class rachunek():
    def __init__(s,nr_rach):
        s.nr_rach=nr_rach
        s.saldo=float(0)
    def wplac(s,kwot):
        s.saldo+=kwot
    def wyplac(s,kwot):
        if kwot>s.saldo:
            print("Niewystarczająca ilość środków na rachunku")
        else:
            s.saldo-=kwot
    def info(s):
        print('Rachunek nr: ',end='')
        x=str(s.nr_rach)
        print(f'{x[0]}{x[1]} ',end='')
        for i in range(2,len(x)-5,4):
            print(f'{x[i]}{x[i+1]}{x[i+2]}{x[i+3]} ',end='')
        print()
        print(f'Saldo {s.saldo} zl')
x=rachunek(12345655559090111100007722)
x.info()
x.wplac(25.30)
x.info()
x.wplac(31.70)
x.info()
x.wyplac(14)
x.info()
'''
#20
#21
class statystyka():
    def __init__(s,tab):
        s.liczby=tab
    def dodaj(s,liczb):
        s.liczby.append(liczb)
    def wysw(s):
        for i in s.liczby:
            print(f'{i} ',end='')
    def najwie(s):
        najw=s.liczby[0]
        for i in s.liczby:
            if i>najw:
                najw=i
        return najw
    def najmnie(s):
        najm=s.liczby[0]
        for i in s.liczby:
            if i<najm:
                najm=i
        return najm
    def srednia(s):
        suma=0
        for i in s.liczby:
            suma+=i
        return suma/len(s.liczby)
    def mediana(s):
        x=copy.deepcopy(s.liczby)
        x.sort()
        if len(x) %2==0:
            return (x[(int(len(x)/2))]+x[(int(len(x)/2)+1)])/2
        else:
            return x[int(len(x)/2)]
    def wyswielkstat(s):
        print(s.najmnie())
        print(s.najwie())
        print(s.srednia())
        print(s.mediana())
x=statystyka([12,37,6,9,17])

x.wyswielkstat()