import math, random
"""# z.10
x=7
y=34
print("x = ",x)
print("y = ",y)

z=7
x=34
y=z
print("x = ",x)
print("y = ",y)

#z.11
liczby = [5,1,8,6,3]
    #a 

    #b
wynik=0
for i in liczby:
    wynik += i*i
print(wynik)
    #f
print(liczby[0]%3)
    #h
print(liczby[3]<<2)

#z.12

uczelnia='Uniwersytet Ekonimiczny w Krakowie'
print(uczelnia)
print(len(uczelnia))
print (uczelnia[0])
print(uczelnia[len(uczelnia)-1])
print(uczelnia[3:11])

#z.13
imiona=["Jan","Dariusz","Marcin"]
    #a
print(len(imiona))
    #b
print(imiona[0])
    #c
print(imiona[len(imiona)-1])

#z.14
liczby=[2,7,3,5]
print(liczby[1])
suma14=0
for i in liczby:
    suma14+=i
print(suma14)
print(len(liczby))
print(liczby[len(liczby)-2])
print(suma14/len(liczby))

# z.15
liczba=int(input())
print(f'Warosc liczby to {liczba},a {liczba**2} to jej potega')

#z17
x17=15.84
print(f"Kwota: {x17}  Podatek : {round(x17 * 0.23,2)}")

#z19
x19=int(input())
y19=int(input())
print(x19+y19)

#z20
r20=5
print("pole: ",math.pi*(r20**2) )
print("obwod: ", 2 * math.pi*r20)

#21
x21=int(input())
sprint(f"Fahrenheit: {x21*9/5 +32} ",f"Kelvin: {x21+273.15} " )

#22
a22=int(input())
b22=int(input())
c22=int(input())
s=(((a22+b22+c22)*(a22+b22-c22)*(a22-b22+c22)*(-a22+b22+c22))**(1/2))/4
print(s)

#24
print("Podaj wzrost w cm")
x=int(input())
y=x/2.54
print(f"Mam {x} cm wzrostu, tj {y//12} stop i {round(y%12)} cali")

#z25
rach=list(input())
print(f"Nr rachunku: {rach[0]}{rach[1]} ", end='')
for x in range(2,len(rach)):
    if x%4 ==2:
        print(" ",end='')
    print(rach[x],end='')

#26
height26=int(input())
weight26=int(input())
print(f'{weight26/(height26/100)**2}')


#z27
lica=int(input())
licb=int(input())
print(f"Najwiekszy wspólny dzielnik liczb: {lica}, {licb} :",math.gcd(lica,licb))

#28
kostka1=random.randint(1,6)
kostka2=random.randint(1,6)
kostka3=random.randint(1,6)
print("Wyrzucone liczby: ",kostka1,kostka2,kostka3 )
print("Suma wyrzuconych oczek: ", kostka1+kostka2+kostka3 )

#29
kostkacpu=random.randint(1,6)
odp=int(input())
print( odp==kostkacpu )

#30
tab30=[12,6,4,9,3]
for x in tab30:
    print(x ,": ",'*'*x)
"""