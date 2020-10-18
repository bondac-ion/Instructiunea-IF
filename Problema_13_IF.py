"""La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? Exemplu : date de intrare : x=38 date de ieşire :
rosie. """
x=int(input("dati locul lui Ionel:"))
if x%4==0:
    print("culoarea neagra")
elif x%2==0:
    print("culoarea rosie")
elif (x+1)%4==0:
    print("culoarea albastra")
else:
    print("culoarea alba")    