""" Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
Nr. bile albe mari: 3 Nr. bile rosii mici: 1 Nr. bile rosii mari: 4 Nr. bile verzi mici: 3 Nr. bile verzi mari: 4 Date de ieşire Totalul
bilelor: 17 Mari: 11 bile Verzi: 7 bile ."""
a_x=int(input("nr. de bile albe mici:"))
r_x=int(input("nr. de bile rosii mici:"))
v_x=int(input("nr. de bile verzi mici:"))
a_y=int(input("nr. de bile albe mari:"))
r_y=int(input("nr. de bile rosii mari:"))
v_y=int(input("nr. de bile verzi mari:"))
xt=a_x+r_x+v_x
yt=a_y+r_y+v_y
print("totalul bilelor:",xt+yt)
if xt>yt:
    print("bile mici",xt)
elif yt>xt:
    print("bile mari:",yt)
else:
    print("nr. bilelor este egal:",xt)
if (a_x+a_y)>(r_x+r_y) and (a_x+a_y)>(v_x+v_y):
    print("Albe:",a_x+a_y)
elif (r_x+r_y)>(a_x+a_y) and (r_x+r_y)>(v_x+v_y):
    print("Rosii:",r_x+r_y)
elif (v_x+v_y)>(r_x+r_y) and (v_x+v_y)>(a_x+a_y):
    print("Verzi:",v_x+v_y)
elif (a_x+a_y)==(r_x+r_y) and (a_x+a_y)>(v_x+v_y) and (r_x+r_y)>(v_x+v_y):
    print("Albe si Rosii au acelasi numar:",a_x+a_y)
elif (a_x+a_y)==(v_x+v_y) and (a_x+a_y)>(r_x+r_y) and (v_x+v_y)>(r_x+r_y):
    print("Albe si Verzi au acelasi numa:r",a_x+a_y)
elif (v_x+v_y)==(r_x+r_y) and (v_x+v_y)>(a_x+a_y) and (r_x+r_y)>(a_x+a_y):
    print("Verzi si Rosii au acelasi numar:",r_x+r_y)
else:
    print("Albe, Rosii si Verzi au acelasi numar:",a_x+a_y)