import csv
import pandas as pd
from pandas import *
import numpy as np
import matplotlib.pyplot as plt

aux = 0
dados = []
dados_norm = []
numero_de_leituras = 25 #Número de leituras que você quer plotar

# Pegando os dados
df = pd.read_csv('Tensao_esp.csv')
dados = df['dados'].values.tolist()

while (aux < numero_de_leituras):
    dados_norm.append(float(dados[aux])*40)
    aux = aux + 1

# Linha de "tempo"
x = np.arange(0, 0.1 * numero_de_leituras, 0.1)

# Plotando o CSV
plt.plot(x, dados_norm)
plt.title('Temperatura')