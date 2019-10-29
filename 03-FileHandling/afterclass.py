import re
'''
#18
tab18=[]
with open('numbers.txt','r') as f18:
    for i in f18:
        i=i.strip('\n')
        tab18.append(int(i))
tab18.sort()
print(tab18)

#19
tab19=[]
with open('universities.txt','r') as f19:
    for i in f19:
        tab19.append(i)
tab19.sort()
with open('universities.txt','w') as f19:
    for i in tab19:
        f19.write(i)

#20
tab20=[]
with open('numbers.txt','r') as f20:
    for i in f20:
        i=i.strip('\n')
        tab20.append(int(i))
with open('evennumbers.txt','w') as f20:
    for i in tab20:
        if i %2 ==0:
            f20.write(f'{i}\n')

#21
tab21=[]
suma21=0
with open('numbersinrows.txt','r') as f21:
    for i in f21:
        i=i.strip('\n')
        i=i.split(",")
        for j in i:
            suma21+=int(j)
            tab21.append(j)
print(len(tab21))
print(suma21)

#22
tab22=[]
with open('students.txt','r') as f22:
    for i in f22:
        i=i.strip('\n')
        i=i.split(",")
        tab22.append(i)
p22=0
for i in tab22:
    if p22==0:
        p22+=1
        continue
    if int(i[2])<30:
        print(i[0],i[1],i[4])

#23
cyfry23=[]
with open('land.txt','r') as f23:
    for i in f23:
       cyfry23+=re.findall('\d',i)
suma23=0
for i in cyfry23:
    suma23+=int(i)
print(suma23)

#24
tab24=[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
with open('zad24.txt','w') as f24:
    p24=0
    for i in tab24:
        for j in i:
                f24.write(j)
                if p24!=2:
                    f24.write(',')
                    p24+=1
                else:
                    p24=0
        f24.write('\n')
'''