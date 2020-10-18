""")“Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă
iubeşte …. Exemplu: Date de intrare: x=10 Date de ieşire: … de loc."""
a=int(input("dati un numar:"))
if a%5==0:
    print("de loc")
elif a%4==0:
    print("la nebunie")
elif a%3==0:
    print("cu pasiune")
elif a%2==0:
    print("mult")
else:
    print("un pic")