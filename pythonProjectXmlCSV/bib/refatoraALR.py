
import pandas as pd
import regex as re

class RefatoraALR:

    def __init__(self, nomeCsv="", Area = "", texto = ""):

        print("Instanciada\n")

        self.auxNome = nomeCsv

        print(self.auxNome[11: (self.auxNome.rfind("."))])

        xml_TXT = open(texto, "r+", encoding = 'cp850')
        textoXML = str("".join(xml_TXT.readlines()))
        print(textoXML)
        #######################################################
        auxDB = pd.read_excel(self.auxNome)
        print(auxDB.head(20))
        print("\n\n\n")

        for i in range(len(auxDB)):
            print("Concatenando ", auxDB.loc[i, 'Name'], " com : ", Area)

            apontamentoC = Area + auxDB.loc[i, 'Name']

            src_str = re.compile(re.escape(auxDB.loc[i, 'Name']), re.IGNORECASE)
            textoXML = src_str.sub(apontamentoC, textoXML)

            print(auxDB.loc[i, 'Name'] + ": OK")

        print("carregamento de dados de Tabela completo\n")

        xml_TXT.seek(0)
        xml_TXT.write(textoXML)
        xml_TXT.truncate()
        xml_TXT.close()






