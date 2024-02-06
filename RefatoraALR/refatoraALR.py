
import pandas as pd


class RefatoraALR:

    def __init__(self, nomeCsv="", Area = ""):

        print("Instanciada\n")

        self.auxNome = nomeCsv

        print(self.auxNome[11: (self.auxNome.rfind("."))])

        auxDB = pd.read_excel(self.auxNome)
        print(auxDB.head(20))
        print("\n\n\n")

        for i in range(len(auxDB)):

                    print("Concatenando ", auxDB.loc[i, 'Name'], " com : ", Area)

                    auxDB.loc[i, 'Name'] = Area + auxDB.loc[i, 'Name']
                    print(auxDB.loc[i, 'Name'] + ": OK")

        auxDB.to_excel("./Database/" + str(self.auxNome[11: (self.auxNome.rfind("."))]) + "_alarRefactory.xls",
                       index=False)
        print("carregamento de dados de Tabela completo\n")







