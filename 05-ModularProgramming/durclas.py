import math
import statistics
#4
'''
x,y=3.7,4
print(math.sqrt(x))
print(math.sqrt(y))
print(math.pow(x,y))
print(math.pi*y**2)
print(math.factorial(y))
print(math.floor(x))

#5
tab5=[21600,4350,3920,5590,3250,4010]
print(statistics.mean(tab5))
print(statistics.median(tab5))
print(statistics.pstdev(tab5))

#6
import csv
with open('employees.csv', 'r') as f:
        reader=csv.reader(f)
        k=0
        tab=[]
        for i in reader:
            print(f'{k:<5}',end='')
            z=0
            for j in i:
                print(f'{j:<15}',end='')
                if z==2 and k!=0:
                    tab.append(int(j))
                z+=1
            k+=1
            print()
        print(statistics.mean(tab))

#7
import square
'''

#11