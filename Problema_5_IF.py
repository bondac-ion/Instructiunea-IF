"""Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. Exemplu : Date
de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani. """
a_curent=int(input("dati anul curent:"))
l_curenta=int(input("dati luna curenta:"))
z_curenta=int(input("dati ziua curenta:"))
a_nasterii=int(input("dati anul nasterii:"))
l_nasterii=int(input("dati luna nasterii:"))
z_nasterii=int(input("dati ziua nasterii:"))
if l_curenta>l_nasterii:
    print(a_curent-a_nasterii,"ani")
elif l_nasterii>l_curenta:
    print(a_curent-a_nasterii-1,"ani")
elif (l_curenta==l_nasterii) and z_curenta>z_nasterii:
    print(a_curent-a_nasterii,"ani")
elif (l_curenta==l_nasterii) and (z_curenta==z_nasterii):
    print(a_curent-a_nasterii,"ani")
else:
    print(a_curent-a_nasterii-1,"ani")