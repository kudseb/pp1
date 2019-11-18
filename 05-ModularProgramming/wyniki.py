def pokazWyniki(dane,oblicz):
    print('RAPORT Z WYDATKOW')
    mies=['styczen','luty','marzec','kwiecien','maj','czerwiec']
    stat=['srednia','mediana','min','max']
    print(f'{"MIESIAC":<10} {"WYDATKI":<10}')
    for i in range(0,7):
        print(f'{mies[0]:<15}{dane[0]:<15}')
    print()
    print('STATYSTYKA WYDATKOW')
    for i in range(0,5):
        print(f'{stat[0]:>15}{oblicz[0]:>15}')
        print()
    for i in range(0,7):
        print(f'{mies[0]:<15}')
        
    
