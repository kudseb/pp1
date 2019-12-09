
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

'''
#11
class Arrays():
    @staticmethod
    def pirnt_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_coma(array):
        print(f'{array[0]}',end='')
        for i in range(1,len(array)):
            print(f', {array[i]}',end='')
    @staticmethod
    def 
            
my_array=[4,1,8,7,2]
Arrays.pirnt_in_col(my_array)
Arrays.print_coma(my_array)