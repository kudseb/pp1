import math
#5
'''
a=5
b=0
assert b!=0, 'WArtosc b rowna 0'
print(f'{a}/{b} = {a/b}')

#6
a=input("Podaj wartosc a: ")
b=input("Podaj wartosc b: ")
print(type(int(b)))
assert int(b) and int(a), 'Liczbt naturalne proszę' #zero nie działa bo zwraca 0 a zero jest false
a=int(a)
b=int(b)
assert b!=0,'Nie dzielimy przez 0'
print(f'{a}/{b} = {a/b}')

#7
wzrost=int(input('Podaj wzrost w cm: '))
waga=float(input('Podaj wage w kg: '))
assert wzrost<220 and wzrost>150, 'Wzrost nie w przedziale'
assert waga<150 and waga>40, 'waga nie w przedziale'
bmi=round(waga/(wzrost/100)**2,4)
print(f'Twoje bmi to : {bmi}')


#8
while True:
    try:
        number=float(input('Enter any number:'))
        print(f'sqrt{number} ={math.sqrt(number)}')
        break
    except:
        print('Please enter a valid number greater than 0')

#9
try:
    with open('NoEducation.txt') as plik :
        for i in plik:
            print(i)
except:
    print('Nie udało się otworzyć pliku, może nie istnieje ')
'''
#10