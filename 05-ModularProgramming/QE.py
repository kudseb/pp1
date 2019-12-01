def qe():
    # odczytaj współczynniki z klawiatury, zwraca tablicę współczynników
    def czytajWspolczynniki():
        return [float(input('Podaj ws a:')),float(input('Podaj ws b:')),float(input('Podaj ws c:'))]
    # oblicz deltę
    def obliczDelte(tab):
        return  (tab[1]**2+4*tab[0]*tab[2])**(1/2)
    #wyznacz pierwiastki równania - zwraca tablicę pierwiastków (jeden lub dwa elementy) lub pustą tablicę, jeśli delta < 0
    def obliczPierwiastki(tab):
        delta=obliczDelte(tab)
        if delta == 0:
            return [(-tab[1])/(2*tab[0])]
        elif delta >0:
            return[(-tab[1]-delta)/(2*tab[0]),(-tab[1]+delta)/(2*tab[0])]
        else:
           return []
    # wyświetl wyznaczone pierwiastki równania kwadratowego
    def wyswietlPierwiastki(tab):
        for i in tab:
            print(round(i,2))
    x=czytajWspolczynniki()
    x=obliczPierwiastki(x)
    wyswietlPierwiastki(x)
