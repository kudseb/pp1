import re
#8/9
'''
f5=open('NoEducation.txt','r')
i5=1
for li in f5:
    print(i5,li,end='')
    i5+=1
f5.close()

#10
suma10=0
with open('numbers.txt','r') as f10:
    for i in f10:
        suma10+=int(i)
print(suma10)

#11
with open('PersonalData.txt','w') as f11:
    f11.write('Sebastian Kudła \nUEK\nInformatyka stosowana \n')
#12

with open('shoppinglist.txt','a') as f12:
    f12.write(input('Podaj nazwe produktu: '))
    f12.write('\n')
#13

tab13=[32,16,5,8,24,7]
with open('zad13.txt','w') as f13:
    for i in tab13:
        f13.write(f'{i}\n')

#14
# ".*"
#"Poland"
#"Poland | Germany | France"
#"[a-zA-z]"
#"[A-z]"
#"\d"
#"\D"
#"\s"
#
#"\d{4}"
#"\d*%"
#"[,.]"
#"[a-zA-z']*"
#"\bn|N"
#"\b[a-zA-z]{3}\b"
#"\b[a-zA-z]{5,}\b"
#"\b[A-Z]"

#16
temp15='wtorek - 23C, środa - 21C, czwartek 25C'
x=re.findall("\d{2}",temp15)
srednia=0
for i in x:
    srednia+=int(i)
srednia/=len(x)
print(srednia)

#17
reg='[aeyioąęuó]'
txt='To be, or not to be, that is the question'
spam=re.findall(reg,txt)
print(len(spam))
'''
