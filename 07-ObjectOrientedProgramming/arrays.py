import random
class Arrays():
    separator=','
    @staticmethod
    def change_separator(new_separ):
        Arrays.separator=new_separ
    @staticmethod
    def pirnt_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_coma(array):
        print(f'{array[0]}',end='')
        for i in range(1,len(array)):
            print(f'{Arrays.separator} {array[i]}',end='')
        print()    
    @staticmethod
    def create_tab(l_elem,tab_val):
        tab=[]
        for i in range(l_elem):
            tab.append(tab_val)
        return tab
    @staticmethod
    def create_tab_from_to(liczba_elementow_tablicy,wartosc_od,wartosc_do):
        tab=[]
        for i in range(liczba_elementow_tablicy):
            x=random.randint(wartosc_od,wartosc_do)
            tab.append(x)
        return tab
    @staticmethod
    def find_elem(tab,wartosc_od,wartosc_do):
        found=0
        for i in tab:
            if i<=wartosc_do and i>=wartosc_od:
                found+=1
        return found
my_array=[4,1,8,7,2]
Arrays.pirnt_in_col(my_array)
Arrays.print_coma(my_array)
#print(Arrays.create_tab(3,2))
#print(Arrays.create_tab_from_to(10,0,1))
#print(Arrays.find_elem(my_array,1,3))
Arrays.change_separator(';')
Arrays.print_coma(my_array)