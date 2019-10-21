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
#z.13
imiona=["Jan","Dariusz","Marcin"]
    #a
print(len(imiona))
    #b
print(imiona[0])
    #c
print(imiona[len(imiona)-1])
# z.15
liczba=int(input())
print(f'Warosc liczby to {liczba},a {liczba**2} to jej potega')

#z25
rach=list(input())
print(f"Nr rachunku: {rach[0]}{rach[1]} ", end='')
for x in range(2,len(rach)):
    if x%4 ==2:
        print(" ",end='')
    print(rach[x],end='')
    

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