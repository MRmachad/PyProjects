import datetime

class Holder():

    def __init__(self):
        self.G_ID = 0
        self.G_DAT = ["guarda data e hora"]
       

    def pega_data(self,G_DATF="2022-7-22_2:6:2"):

        date = []

        for i in range(G_DATF.count("_")):
            date.append(G_DATF[:G_DATF.find("_")])
            G_DATF = G_DATF[G_DATF.find("_") + 1:]


        v_data = [
            int(date[0]), \
            int(date[1]), \
            int(date[2]), \
            int(date[3]), \
            int(date[4]), \
            int(date[5]), \
            int(G_DATF),
            ]
        return v_data

    def setDateID(self, G_ID_p = "0", G_DATF_p="2022-7-22_2:7:2", G_DATI_p="2022-7-22_2:6:2", lenraw=170):

        print("entrou na SETdateID", G_ID_p,", ", G_DATF_p,", ", G_DATI_p,", ", lenraw,"\n\n")

        v_dataF = self.pega_data(G_DATF_p)
        v_dataI =self.pega_data(G_DATI_p)

        dataAjuste = datetime.timedelta(hours=3)

        dataF = datetime.datetime(v_dataF[0], v_dataF[1], v_dataF[2], v_dataF[3], v_dataF[4], v_dataF[5], v_dataF[6] )-dataAjuste

        dataI = datetime.datetime(v_dataI[0], v_dataI[1], v_dataI[2], v_dataI[3], v_dataI[4], v_dataI[5], v_dataI[6])-dataAjuste



        lenraw_entreMeio = lenraw - 1

        diferenca = (dataF - dataI) / (lenraw_entreMeio)

        self.G_DAT = [dataI.strftime("%Y-%m-%d %H:%M:%S.%f")]

        for i in range(lenraw_entreMeio-1):
            dataI = (dataI + diferenca)
            self.G_DAT.append(str(dataI))

        self.G_DAT.append(dataF.strftime("%Y-%m-%d %H:%M:%S.%f"))

        self.G_ID = G_ID_p


    def juntalinhas(self, accX=[], accY=[], accZ=[]):

        print("\nentrou na juntalinhas", self.G_ID, ", ", len(self.G_DAT), ", ",
              len(accX), ", ", len(accY), ", ",len(accZ), "\n\n")

        record_to_insert = []
        for i in range(len(accX)):
            record_to_insert.append((self.G_ID,self.G_DAT[i], accX[i], accY[i], accZ[i]))

        self.G_DAT = self.G_DAT[len(accX):]

        accX, accY, accZ = [], [], []

        print("saiu da juntalinhas", self.G_ID, ", ", len(self.G_DAT), ", ",
              len(accX), ", ", len(accY), ", ",len(accZ), "\n\n")

        return record_to_insert

