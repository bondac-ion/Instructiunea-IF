"""Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?
Exemplu : date de intrare : n=69 date de ieşire : casuta 17."""
n=int(input("locul sosorii lui Ionel:"))
if n<=4:
    print("casuta 1")
else:
    print("casuta",n//4+1)