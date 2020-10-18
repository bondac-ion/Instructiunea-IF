"""Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau
IMPAR. Exemplu : Date de intrare : 45 3 24 Date de ieşire : 45 impar 3 impar 24 par."""
a=int(input("dati un numar"))
b=int(input("dati un numar"))
c=int(input("dati un numar"))
if a%2==0:
    print(a," par")
else:
    print(a," impar")
if b%2==0:
    print(b," par")
else:
    print(b," impar")
if c%2==0:
    print(c," par")
else:
    print(c," impar")