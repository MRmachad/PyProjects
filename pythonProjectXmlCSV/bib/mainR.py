import os


import refatoraALR

if __name__ == '__main__':
    Vdir = []
    Dbase = []
    bases_dic = './Database'

    for diretorio, subpastas, arquivos in os.walk(bases_dic):
        for arquivo in arquivos:
            Dbase.append(os.path.join(diretorio, arquivo))


    DbALR = []
    bases_alr = './dbalrm'

    for diretorio, subpastas, arquivos in os.walk(bases_alr):
        for arquivo in arquivos:
            DbALR.append(os.path.join(diretorio, arquivo))

#Abrir o alarme tag do ft em texto

    for DbTag in Dbase:
        for alrTXT in DbALR:
            print(DbTag)
            print(alrTXT)
            area = input("\n Concatena com o que? \n")
            ob = refatoraALR.RefatoraALR(str(DbTag), area, alrTXT)
            break
