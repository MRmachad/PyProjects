def pega_data(G_DATF = "2022-7-22_2:6:2"):
    v_data = [
        int(G_DATF[:G_DATF.find("-")]),\
    int(G_DATF[G_DATF.find("-") + 1:G_DATF.rfind("-")]),\
    int(G_DATF[G_DATF.rfind("-") + 1:G_DATF.find("_")]),\
    int(G_DATF[G_DATF.find("_") + 1:G_DATF.find(":")]),\
    int(G_DATF[G_DATF.find(":") + 1:G_DATF.rfind(":")]),\
    int(G_DATF[G_DATF.rfind(":") + 1:])
            ]
    return v_data


G_DATI = "2022-7-22_2:14:26"
G_DATF = "2022-7-22_2:15:14"


import datetime

v_dataF = pega_data(G_DATF)
v_dataI = pega_data(G_DATI)

dataF = datetime.datetime(v_dataF[0], v_dataF[1], v_dataF[2], v_dataF[3], v_dataF[4], v_dataF[5])

dataI = datetime.datetime(v_dataI[0], v_dataI[1], v_dataI[2], v_dataI[3], v_dataI[4], v_dataI[5])
print(dataI.microsecond)

lenraw = 342
lenraw_entreMeio = lenraw - 2
diferenca = (dataF-dataI)/(lenraw_entreMeio)

print(diferenca)

G_DAT = [dataI.strftime("%m-%d-%Y %H:%M:%S")]

for i in range(lenraw_entreMeio):
    dataI = (dataI + diferenca)
    G_DAT.append(dataI.strftime("%m-%d-%Y %H:%M:%S")+"."+ str(dataI.microsecond)[0:4])
    print("while")

G_DAT.append(dataF.strftime("%m-%d-%Y %H:%M:%S"))

print((G_DAT[300]))
print(len(G_DAT))
