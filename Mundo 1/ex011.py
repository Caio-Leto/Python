from traceback import print_tb


larg = float(input("largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
print("Sua parede tem a dimensão de {}x{} e sua área de {}m².".format(larg, alt, area))
tinta = area / 2
print("Para pintar a parede você precisa de {}L de tinta".format(tinta))