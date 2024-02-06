import numpy as np
import matplotlib.pyplot as plt

x=0

fig=plt.figure()
grafico=fig.add_subplot(111)


i = 0

grafico.scatter([i,i], [i+1,i+2])
plt.title("Real Time plot")
plt.xlabel("x")
plt.ylabel("sinx")

plt.show()

i = 1

grafico.scatter([i,i], [i+1,i+2])
grafico.plot()




