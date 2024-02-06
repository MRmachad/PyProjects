import os


import refatoraALR

if __name__ == '__main__':
    Vdir = []
    Dbase = []
    bases_dic = './Database'

    for diretorio, subpastas, arquivos in os.walk(bases_dic):
        for arquivo in arquivos:
            Dbase.append(os.path.join(diretorio, arquivo))


    for DbTag in Dbase:
        print(DbTag)
        area = input("\n Concatena com o que? \n")
        ob = refatoraALR.RefatoraALR(str(DbTag), area)
        ob.percor()