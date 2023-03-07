import math
import matplotlib.pyplot as plt
import numpy as np

ANGL_PHI = 14

x1 = np.arange(1,31)
x2 = np.arange(0.2, 6.2, 0.2)

def matplot(x1, x2, angl_phi = ANGL_PHI):
    fig, ax = plt.subplots(1, 2, figsize=(18, 9))
    #AX1
    ax[0].plot(x1, y_line(x1, angl_phi), color='red', marker='.', linestyle='None', markersize = 5.0)
    ax[0].set_title('График от функции с частотой дискритизации 1')
    #AX2
    ax[1].plot(x2, y_line(x2, angl_phi),  color='blue', marker='.', linestyle='None', markersize = 5.0)
    ax[1].set_title('График от функции с шагом дискретизации 0.2')

    for ax in ax.flat:
        ax.set(xlabel='x', ylabel='f(x)')

    plt.show()
    
    

def y_line(x, angl_phi):
    y = []
    for i in range(len(x)):
        y.append(5.18*math.cos(angl_phi*math.pi/180)
                +math.log(abs(math.tan(x[i]/2)))
                +x[i]**2.6/(1+ x[i]/(1+x[i]))
                +(math.log(x[i]**2 + 1, 5))**(1/3))
    return y



if __name__ == "__main__":
    matplot(x1,x2)

