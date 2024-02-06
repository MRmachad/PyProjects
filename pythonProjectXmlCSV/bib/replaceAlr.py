from numpy import NaN
import pandas as pd
import regex as re
from pandas import DataFrame


class ReplaceAlr:
    def __init__(self, nomeCsv="DP-Tags.xlsm", Valr=[])  :

        print("Instanciada\n")

        self.auxNome = nomeCsv

        self.tbTag = self.column_of_csv(" Tag Name").tolist()


        self.tbNode = self.column_of_csv(" Node Name").tolist()


        self.tbAdress = self.column_of_csv(" Address").tolist()

        self.limpaNAN()

        self.verificaComum()

        with open("TAG_" + "_log.txt", "a+") as log:
            for idx in range(len(self.tbTag)):
                print("IDX: " + str(idx) + "\n", file=log)
                print((self.tbTag[idx] + "--->" + self.tbNode[idx] + "--->" + self.tbAdress[idx] + "\n\n"), file=log)

        print("carregamento de dados de Tabela completo\n")

        self.baseAlr = Valr


    def limpaNAN(self):

        while NaN in ((self.tbTag) and (self.tbNode) and (self.tbAdress)):
            for idx in range(len(self.tbTag)):
                if pd.isna(self.tbTag[idx]) or pd.isna(self.tbNode[idx]) or pd.isna(self.tbAdress[idx]):
                    self.tbTag.pop(idx)
                    self.tbNode.pop(idx)
                    self.tbAdress.pop(idx)
                    break


    def verificaComum(self):

        auxTbTag, auxTbNode, auxTbAdress = [], [], []
        for idx1 in range(len(self.tbTag)):
            for idx2 in range(len(self.tbTag)):
                if str(self.tbTag[idx1]) in str(self.tbTag[idx2]):
                    if (idx1 != idx2):
                        auxTbTag.append(self.tbTag[idx1])
                        auxTbNode.append(self.tbNode[idx1])
                        auxTbAdress.append(self.tbAdress[idx1])
                        self.tbTag[idx1] = "*00000*"
                        self.tbNode[idx1] = "*00000*"
                        self.tbAdress[idx1] = "*00000*"
                        break

        while "*00000*" in self.tbTag:
            self.tbTag.remove("*00000*")
            self.tbNode.remove("*00000*")
            self.tbAdress.remove("*00000*")

        for idx in range(len(auxTbTag)):
            self.tbTag.append(auxTbTag[idx])
            self.tbNode.append(auxTbNode[idx])
            self.tbAdress.append(auxTbAdress[idx])


    def column_of_csv(self, column):

        reader = pd.read_excel(self.auxNome)

        auxV = reader[column].loc[0:len(reader)]
        return auxV


    def percor(self):

        with open(("Alarme_log.txt"), "a+") as log:

            auxAlr = pd.read_excel(self.baseAlr[0])
            print(type(auxAlr))
            print(auxAlr.head(20))
            print(auxAlr.columns )
            print("\n\n\n")


            for i in range(len(auxAlr)):
                print(auxAlr.loc[i, 'Unnamed: 1'])
                for iTag in range(len(self.tbTag)):
                    if str(self.tbTag[iTag]).lower() in str(auxAlr.loc[i,'Unnamed: 1']).lower():
                        auxAlr.loc[i, 'Unnamed: 1'] = ("{/Area1/Data1::[" + str(self.tbNode[iTag]) + "]" + str(self.tbAdress[iTag]) +"}")
                        print(("REPLACE:  " + self.tbTag[iTag] + " --> " + self.tbNode[iTag] + "-->" + self.tbAdress[iTag]+"\n"), file = log)

                        #replace here
                        pass




            auxAlr.to_excel('./alr/alarmesReplace.xlsx', index = False)
            print("\n \n \n \n \n \n" + "Busca por replace encerrada" + "\n \n \n \n \n \n")





