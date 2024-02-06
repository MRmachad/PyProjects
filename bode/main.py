import numpy
import scipy
from numpy.distutils.from_template import conv
from scipy import signal
import matplotlib.pyplot as plt

def valoresBode(num = [], den = []):


    sys = signal.TransferFunction(num, den)
    print(sys)

    w = [(10 ** (-4)), (10 ** (-3)), (10 ** (-2)), (10 ** (-1)), (10 ** (0)), (10 ** (1)), (10 ** (2)), (10 ** (3)),(10 ** (4)), (3), 2]
    w, mag, phase = signal.bode(sys, w)

    for i in range(len(w)):
        print("W = ", w[i], "mag = " , round(mag[i],3), "fase = ", round(phase[i],3), "\n")

    return  mag, phase

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    w = [(10 ** (-4)), (10 ** (-3)), (10 ** (-2)), (10 ** (-1)), (10 ** (0)), (10 ** (1)), (10 ** (2)), (10 ** (3)),(10 ** (4)), (3), 2]
    #teste = numpy.convolve([1, 0], [1, 1, 0])
    #print(teste)

    m2 , p2 = valoresBode([1], [(0.5), 1])
    m2, p2 = valoresBode([1], [(0.25), 1])


