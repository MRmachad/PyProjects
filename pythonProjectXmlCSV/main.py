import os
import formataDB
import replaceTag

if __name__ == '__main__':

    Vdir = []
    Dbase = []
    bases_dic = './Database'

    for diretorio, subpastas, arquivos in os.walk(bases_dic):
        for arquivo in arquivos:
            Dbase.append(os.path.join(diretorio, arquivo))
    print(Dbase)


    selectCV = int(input("Escolha de converção: (1-Database, 2-Display) \n"))

    if selectCV == 2 :

        pasta = './displays'
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                Vdir.append(os.path.join(diretorio, arquivo))
        print(Vdir)

        i = 0
        for DBxlms in Dbase:
            ob = replaceTag.ReplaceTag(str(DBxlms), Vdir, i)
            ob.percor()
            i += 1

    elif selectCV == 1 :

        for DbTag in Dbase:
            ob = formataDB.py.FormataDB(str(DbTag))
            ob.percor()

    else: pass





