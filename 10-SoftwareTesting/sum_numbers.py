# Sumuje liczby nturalne parzyste z przedziału <from_n,to_n>
def sum_even(from_m,to_n):
    if type(from_m) is not int:
        raise ValueError('Liczby naturalne')
    if type(to_n) is not int:
        raise ValueError('Liczby naturalne')
    if from_m <0:
        from_m=0
    sum = 0
    for i in range(from_m,to_n+1):
        if i%2 == 0: # liczba parzysta
            sum += i
    return sum

def main():
    m = 1
    n = 5
    print(f"Suma liczb naturalnych parzystych z przedziału <{m},{n}> wynosi {sum_even(1,5)}")

if __name__ == "__main__":
    main()