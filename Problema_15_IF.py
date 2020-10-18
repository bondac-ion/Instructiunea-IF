"""Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În
ce clasa va fi repartizat (A, B, C, D sau E)?. Exemplu : date de intrare : x=73 date de ieşire : C."""
x=int(input("nr. de ordine al mediei:"))
if x>=1 and x<=25:
    print("A")
elif x>25 and x<=50:
    print("B")
elif x>50 and x<=75:
    print("C")
elif x>75 and x<=100:
    print("D")
elif x>100 and x<=125:
    print("E")
else:
    print("nu intra in nici una din clase")