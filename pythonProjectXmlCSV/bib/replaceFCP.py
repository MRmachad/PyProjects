from numpy import NaN
import pandas as pd
import regex as re
from pandas import DataFrame


class ReplaceFCP:
    def __init__(self, nomeCsv="DP-Tags", VstrDisplays=[], rpComum = 0)  :
        print("Instanciada\n")

        self.auxNome = nomeCsv

        self.auxfcpTag = []
        self.auxfcpTagName = []
        self.auxfcpAdress = []
        self.auxfcpNode = []
        self.rpComum = rpComum

        self.tbTag = self.column_of_csv(" Tag Name").tolist()


        self.tbNode = self.column_of_csv(" Node Name").tolist()


        self.tbAdress = self.column_of_csv(" Address").tolist()

        self.verificaFcp()
        self.verificaComum()
        self.verificaComum2()

        with open("TAG_" + "_log.txt", "a+") as log:
            for idx in range(len(self.tbTag)):
                print("IDX: " + str(idx) + "\n", file=log)
                print((self.tbTag[idx] + "--->" + self.tbNode[idx] + "--->" + self.tbAdress[idx] + "\n\n"), file=log)

            for idxf in range(len(self.auxfcpTag)):
                print("IDX__FCP: " + str(idxf) + "\n", file=log)
                print((self.auxfcpNode[idxf] + "--->" + self.auxfcpAdress[idxf] + "--->" + self.auxfcpTagName[idxf] + "\n\n"), file=log)

        print("carregamento de dados de Tabela completo\n")

        self.VstrDisplays = VstrDisplays

    def verificaFcp(self):

        self.limpaNAN()

        for idx in range(len(self.tbTag)):

            texto_1, texto_2, texto_3 = "", "", ""
            auxIdx1 = self.tbTag[idx].rfind("_")

            if auxIdx1 >= 0:

                    auxIdx2 = self.tbAdress[idx].find(".")

                    if auxIdx2 >= 0:

                        for cont in range(auxIdx1):
                            texto_1 += ( self.tbTag[idx][cont] )

                        if texto_1 not in self.auxfcpTag:

                            auxIdx3 = texto_1.rfind("\\")


                            if auxIdx3 >= 0:

                                auxIdx3 +=1
                                while auxIdx3 < (auxIdx1):
                                    texto_3 += texto_1[auxIdx3]
                                    auxIdx3 +=1

                            for cont in range(auxIdx2):
                                texto_2 += (self.tbAdress[idx][cont])

                            self.auxfcpTag.append(texto_1)
                            self.auxfcpTagName.append(texto_3.upper())
                            self.auxfcpAdress.append(texto_2)
                            self.auxfcpNode.append(self.tbNode[idx])
                        else:
                            pass
                    else:
                        pass


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

    def verificaComum2(self):

        auxTbTag, auxTbNode, auxTbAdress, auxTbTagName  = [], [], [], []

        for idx1 in range(len(self.auxfcpTag)):
            for idx2 in range(len(self.auxfcpTag)):
                if str(self.auxfcpTag[idx1]) in str(self.auxfcpTag[idx2]):
                    if (idx1 != idx2):
                        auxTbTag.append(self.auxfcpTag[idx1])
                        auxTbNode.append(self.auxfcpNode[idx1])
                        auxTbAdress.append(self.auxfcpAdress[idx1])
                        auxTbTagName.append(self.auxfcpTagName[idx1])

                        self.auxfcpTag[idx1] = "*00000*"
                        self.auxfcpNode[idx1] = "*00000*"
                        self.auxfcpAdress[idx1] = "*00000*"
                        self.auxfcpTagName[idx1] = "*00000*"
                        break

        while "*00000*" in self.auxfcpTag:
            self.auxfcpTag.remove("*00000*")

            self.auxfcpNode.remove("*00000*")
            self.auxfcpAdress.remove("*00000*")
            self.auxfcpTagName.remove("*00000*")

        for idx in range(len(auxTbTag)):
            self.auxfcpTag.append(auxTbTag[idx])
            self.auxfcpNode.append(auxTbNode[idx])
            self.auxfcpAdress.append(auxTbAdress[idx])
            self.auxfcpTagName.append(auxTbTagName[idx])


    def column_of_csv(self, column):

        reader = pd.read_excel(self.auxNome)

        auxV = reader[column].loc[0:len(reader)]
        return auxV

    def percor(self):

        #onde for zanine separar topico tag e onde não for colocar noe tag
        for xml in self.VstrDisplays:

            with open(( str(self.rpComum) + "_" + xml[11: (xml.rfind("."))] + "_log.txt"), "a+") as log:

                print("No display " + xml + "\n \n \n \n \n \n")
                auxXML = open(xml, "r+", encoding = 'cp850')
                textoXML = str("".join(auxXML.readlines()))

                for idx in range(len(self.auxfcpTag)):

                    print(("," + self.auxfcpTag[idx].lower()))

                    if ("," + self.auxfcpTag[idx].lower() + ",") in textoXML.lower():

                        apontamentoC = "," + self.auxfcpNode[idx] + ", " + self.auxfcpAdress[idx] + ", " + self.auxfcpTagName[idx] + ","
                        src_str = re.compile(re.escape("," + self.auxfcpTag[idx]) + ",", re.IGNORECASE)
                        textoXML = src_str.sub(apontamentoC, textoXML)
                        print(("REPLACE:  " + self.auxfcpTag[idx] + " --> " + apontamentoC + "\n"), file=log)



                ### Replace Comuns

                if (self.rpComum == 0):

                    apontamentoC = "FcpValveCmd /T"

                    src_str = re.compile(re.escape("FcpValveCmd"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpTqCip /T"

                    src_str = re.compile(re.escape("FcpTqCip"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpAcmpCip /T"

                    src_str = re.compile(re.escape("FcpAcmpCip"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpValveMnt	/T"

                    src_str = re.compile(re.escape("FcpValveMnt"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpMotorCmd	/T"

                    src_str = re.compile(re.escape("FcpMotorCmd"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpMotorMnt	/T"

                    src_str = re.compile(re.escape("FcpMotorMnt"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpInvCmd /T"

                    src_str = re.compile(re.escape("FcpInvCmd"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpInvMnt /T"

                    src_str = re.compile(re.escape("FcpInvMnt"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpTqFrmCmd	/T"

                    src_str = re.compile(re.escape("FcpTqFrmCmd"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpCmdConfSelProdL9L3 /T"

                    src_str = re.compile(re.escape("FcpConfCmdSelProdL9L3"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpConfCmd	/T"

                    src_str = re.compile(re.escape("FcpConfCmd"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpManualAuto_fulltag /T"

                    src_str = re.compile(re.escape("FcpAutoManual_fulltag"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpAutoManual	/T"

                    src_str = re.compile(re.escape("FcpAutoManual"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpBloqHab_fulltag	/T"

                    src_str = re.compile(re.escape("FcpHabBloq_fulltag"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpHabBloq	/T"

                    src_str = re.compile(re.escape("FcpHabBloq"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpPidMain	/T"

                    src_str = re.compile(re.escape("FcpPidMain"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpPidEManut /T"

                    src_str = re.compile(re.escape("FcpPidEManut"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpPidETrend /T"

                    src_str = re.compile(re.escape("FcpPidETrend"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "FcpPidE1Main /T"

                    src_str = re.compile(re.escape("FcpPidE1Main"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "AcompCipFalhaTag /T"

                    src_str = re.compile(re.escape("AcompCipFalhaTag"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "Display"

                    src_str = re.compile(re.escape("VbaExec"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    apontamentoC = "/T"

                    src_str = re.compile(re.escape("/T /T"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                    src_str = re.compile(re.escape("/T / T"), re.IGNORECASE)
                    textoXML = src_str.sub(apontamentoC, textoXML)

                print("\n \n \n \n \n \n" + "Busca por replace encerrada" + "\n \n \n \n \n \n")

            auxXML.seek(0)
            auxXML.write(textoXML)
            auxXML.truncate()
            auxXML.close()
