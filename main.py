import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image



def zadanie1():
    print('Zadanie 1')

    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro:")
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
    plt.ylabel('tutaj y')

    plt.axis([0, 6, 0, 20])

    plt.show()

def zadanie2():
    x = np.arange(0, 5.2, 0.2)
    plt.plot(x, x, 'r-', x, x**2, 'bs', x, x**3, 'g^')

    plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])

    plt.ylabel('y')
    plt.xlabel('x')

    plt.plot(x, x, 'r--', label='liniowa')
    plt.plot(x, x**2, 'bs', label='kwadratowa')
    plt.plot(x, x**3, 'g^', label='szescienna')

    plt.legend(loc='upper left')
    plt.title('Wykres 3 linii')

    plt.show()


if __name__ == '__main__':
    #zadanie1()

    zadanie2()