from numpy import abs
def main():
    n = int(input("Введите точность: "))
    pi_corr = 3.1415926535
    pi = 1
    k = 1
    while abs(pi * (12 ** (1/2)) - pi_corr) > 0.1 ** n:
        pi += 1/(((-1) ** k) * (2*k + 1) * (3 ** k))
        print("Итерация {0}: {1}        Погрешность: {2}".format(k, pi * (12 ** (1/2)), abs(pi * (12 ** (1/2)) - pi_corr))) 
        k += 1
if __name__ == "__main__":
    main()