"""Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj. Exemplu : Date de
intrare nr crt 7 punctaj 120 nr crt 3 punctaj 100 nr crt 4 punctaj 119 Date de ieşire punctaj maxim are elevul cu nr crt 7."""
n1=int(input("dati nr. elevului:"))
n2=int(input("dati nr. elevului:"))
n3=int(input("dati nr. elevului:"))
p1=int(input("dati punctajul elevului:"))
p2=int(input("dati punctajul elevului:"))
p3=int(input("dati punctajul elevului:"))
if p1>p2 and p1>p3:
    print("elevul cu numarul:",n1,"are cel mai mare punctaj")
if p2>p3 and p2>p1:
    print("elevul cu numarul:",n2,"are cel mai mare punctaj")
if p3>p2 and p3>p1:
    print("elevul cu numarul:",n3,"are cel mai mare punctaj")
if p1==p2 and p1>p3 and p2>p3:
    print("elevii cu numarul:",n1,",",n2,"au cel mai mare punctaj")
if p2==p3 and p2>p1 and p3>p1:
    print("elevii cu numarul:",n3,",",n2,"au cel mai mare punctaj")
if p1==p3 and p1>p2 and p3>p2:
    print("elevii cu numarul:",n1,",",n3,"au cel mai mare punctaj")
if p1==p2 and p2==p3 and p1==p3:
    print("elevii au punctaj egal")
