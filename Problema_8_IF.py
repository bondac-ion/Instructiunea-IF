"""Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. Exemple : Date de intrare 23 45 Date de
ieşire nu exista numar par ; Date de intrare 28 14 Date de ieşire 28 ; Date de intrare 77 4 Date de ieşire 4."""
a=int(input("dati un numar:"))
b=int(input("dati un numar:"))
if a%2==0 and b%2==0:
    print(max(a,b))
elif a%2==0 and b%2!=0:
    print(a)
elif a%2!=0 and b%2==0:
    print(b)
else:
    print("numerele sunt impare")