import random
import math
#7
'''
class Student():
    licznik=100000
    def __init__(s,imie):
        s.imie=imie
        s.album=Student.licznik
        Student.licznik +=1
    def __str__(s):
        return f'{s.imie} {s.album}'
x=Student('Jan')
y=Student('Bartek')
z=Student('Dawid')
print(x)
print(y)
print(z)


#15
class Ksiazka():
    def __init__(s,tytul,autor,dat_wydania):
        s.tytul=tytul
        s.autor=autor
        s.data_wydania=dat_wydania
    def __str__(s):
        print(s.tytul,end=', ')
        print(s.autor,end=', ')
        return print(s.data_wydania,end=', ')
class Ebook(Ksiazka):
    def __init__(s,tytul,autor,dat_wydania,nazwapliku):
        super().__init__(tytul,autor,dat_wydania)
        s.nazwapliku=nazwapliku
    def __str__(s):
        super().__str__()
        return s.nazwapliku
class Ksiazpapier(Ksiazka):
    def __init__(s,tytul,autor,dat_wydania,liczastron):
        super().__init__(tytul,autor,dat_wydania)
        s.liczastron=liczastron
    def __str__(s):
        super().__str__()
        return str(s.liczastron)
        
x=Ebook('tytul','autor','dwyda','lol.exe')
y=Ksiazpapier('tytul','autor','dwyda',175)
print(x)
print(y)

#16
class Student():
    def __init__(s,imie,nazwisko,nralbum):
        s.imie=imie
        s.nazwisko=nazwisko
        s.nralbum=nralbum
    def __str__(s):
        print(s.imie,end=', ')
        print(s.nazwisko,end=', ')
        return str(s.nralbum)
    def __eq__(s,o):
        return s.nralbum == o.nralbum
    def __lt__(s,o):
        return s.nralbum < o.nralbum
    def __gt__(s,o):
        return s.nralbum > o.nralbum
x=Student('Anna' ,'Tomaszewska', 141820)
x3=Student('Anna' ,'dwada', 141820)
y=Student('Wojciech', 'Zbych' ,201003)
z=Student('Maja', 'Kowalska', 153202)
k=Student('Marek', 'Migiel', 138600)
tab=[x,y,z,k]
tab=sorted([x,y,z,x3,k])
for i in tab:
    print (i)
'''
#17
class pole():
    @staticmethod
    def kolo(promien):
        return round(math.pi * promien**2,3)
    @staticmethod
    def prostokat(lenght,width):
        return round(lenght*width,3)
    @staticmethod
    def trojak(bas,height):
        return round((bas*height)/2,3)

print(pole.kolo(2))
print(pole.prostokat(2,2))
print(pole.trojak(2,2))