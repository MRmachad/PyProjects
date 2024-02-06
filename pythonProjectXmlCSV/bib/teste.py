from numpy import NaN
import pandas as pd
import os
if __name__ == '__main__':

    v = [2,3,5]
    c = [2,3,5]
    print(v)
    tam =len(v)
    for i in range(tam):
        for it in range(tam):
            v.append(0)
            print(len(v))
            print((it))
            print("Vai voltar")

    print(v)

