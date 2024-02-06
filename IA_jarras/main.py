def mover(jarras, cap, pra):

    if pra == 1:
        if (jarras[0] < cap[0] and jarras[1] != 0):
             if ((jarras[1] + jarras[0]) > cap[0]): jarras[0], jarras[1] = cap[0], ((jarras[1] + jarras[0]) - cap[0])
             else: jarras[0], jarras[1] = (jarras[1] + jarras[0]), 0
        else:
            print("Operação nao pode ser realizada")



    if pra == 2:
        if (jarras[1] < cap[1] and jarras[0] != 0):
            if ((jarras[1] + jarras[0]) > cap[1]): jarras[1], jarras[0] = cap[1], ((jarras[1] + jarras[0]) - cap[1])
            else:   jarras[1], jarras[0] = (jarras[1] + jarras[0]), 0


        else:
            print("Operação nao pode ser realizada")

def encher(jarras, cap, pra):

    if pra == 1:
        if (jarras[0]< cap[0]): jarras[0] = cap[0]
        else:
            print("Operação nao pode ser realizada")

    if pra == 2:
        if (jarras[1] < cap[1]): jarras[1] = cap[1]
        else:
            print("Operação nao pode ser realizada")

def esvaziar(jarras, pra):

    if pra == 1:
        if (jarras[0] > 0): jarras[0] = 0
        else:
            print("Operação nao pode ser realizada")

    if pra == 2:
        if (jarras[1] > 0): jarras[1] = 0
        else:
            print("Operação nao pode ser realizada")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    jarras, cap = [], []
    jarras.append(0)
    jarras.append(0)
    cap.append(3)
    cap.append(4)

    print("Estado atual  da jarra", jarras)
    print("Capaciade da Jarra", cap)

    while(jarras[1] != 2):

        r = int(input("\nEscolha Uma ação:\n"
                      "1 - Encher Jarro 1\n"
                      "2 - Encher Jarro 2\n"
                      "3 - Esvaziar jarro 1\n"
                      "4 - Esvaziar jarro 2\n"
                      "5 - Mover do Jarro 2 para o jarro 1\n"
                      "6 - Mover do Jarro 1 para o jarro 2\n\n"))

        if (r == 1):  # Enche j1
            encher(jarras, cap, 1)
            print("Estado atual pos encher 1: (%d, %d)" % (jarras[0], jarras[1]))

        if (r == 2):  # Enche j2
            encher(jarras, cap, 2)
            print("Estado atual pos encher 1: (%d, %d)" % (jarras[0], jarras[1]))

        if (r == 3):  # Esvazia j1
            esvaziar((jarras), 1)
            print("Estado atual pos esvaziar 2: (%d, %d)" % (jarras[0], jarras[1]))

        if (r == 4):  # Esvazia j2
            esvaziar((jarras), 2)
            print("Estado atual pos esvaziar 2: (%d, %d)" % (jarras[0], jarras[1]))

        if (r == 5):  # Passa tudo de j2 para j1
            mover(jarras, cap, 1)
            print("Estado atual pos mover de 1 pra 2: (%d, %d)" % (jarras[0], jarras[1]))

        if (r == 6):  # Passa parte de j1 para j2
            mover(jarras, cap, 2)
            print("Estado atual pos mover de 1 pra 2: (%d, %d)" % (jarras[0], jarras[1]))

        print("Estado atual: (%d, %d) \n" % (jarras[0], jarras[1]))

    print("Resultado Obtido (%d, %d)" % (jarras[0], jarras[1]))






