#24
"""
print("Podaj wzrost w cm")
x=int(input())
y=x/2.54
print(f"Mam {x} cm wzrostu, tj {y//12} stop i {round(y%12)} cali")
"""
#25
print("Podaj nr rachunku bankwego: ")
nrrach=str(input())
print(f"Nr rachunku: {nrrach[0:2]} ", end='')
i=2;
while len(nrrach)<i:
    print(nrrach[i],nrrach[i+1],nrrach[i+2],nrrach[i+3]," ",end='')
    i+=4