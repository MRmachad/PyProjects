from numpy import NaN
import pandas as pd
import regex as re
from pandas import DataFrame


class FormataDB:
    def __init__(self, nomeCsv=""):

        print("Instanciada\n")

        self.auxNome = nomeCsv
        print(self.auxNome[11: (self.auxNome.rfind("."))])
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

        with open(("CV_"+str(self.auxNome[11: (self.auxNome.rfind("."))])+"_log.txt"), "a+") as log:

            auxDB =  pd.read_excel(self.auxNome)
            print(auxDB.head(20))
            print("\n\n\n")

            for i in range(len(auxDB)):

                if range(len(self.tbTag)) != 0:

                    for iTag in range(len(self.tbTag)):
                        print("Procurando por: ",auxDB.loc[i,' Tag Name'], " em : ", self.tbTag[iTag])

                        if str(self.tbTag[iTag]).lower() in str(auxDB.loc[i,' Tag Name']).lower():
                            auxDB.loc[i, ' Address'] = ("/Area1/Data1::[" + str(self.tbNode[iTag]) + "]" + str(self.tbAdress[iTag]))
                            print(("REPLACE:  " + self.tbTag[iTag] + " --> " + self.tbNode[iTag] + "-->" + self.tbAdress[iTag]+"\n"), file = log)

                            del(self.tbTag[iTag])
                            del(self.tbNode[iTag])
                            del(self.tbAdress[iTag])

                            break

                else:
                    break


                auxDB.loc[i, ' Node Name'] = ""


            auxDB.rename(columns = {' Node Name' : ' Retentive'}, inplace=True)
            auxDB = auxDB.drop(columns=[' Data Logged'])
            auxDB = auxDB.drop(columns=[' Scan Class'])


            auxDB.to_excel("./Database/"+ str(self.auxNome[11: (self.auxNome.rfind("."))]) + "_apontamento_direto.xlsx", index = False)

            print("\n \n \n \n \n \n" + "Busca por replace encerrada" + "\n \n \n \n \n \n")





