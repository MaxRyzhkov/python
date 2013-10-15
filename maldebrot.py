from numpy import *
import matplotlib.pyplot as plt

def maldebrot(size, nmax):
    def ijC(i,j):
        k = float(size) / (nmax-1)
        x = k*i - size
        y = k*j - size
        z = x + 1j*y
        return z

    def colorize(i,j):
        z = ijC(i,j)
        color = 0
        c = z
        while (abs(z) < 2 and color < 150):
            z = z*z + c
            color += 1
        return color

    arr = zeros((nmax,nmax))
    for i in range(nmax):
        print (100.0*i/nmax)
        for j in range(nmax):
            arr[i][j] = colorize(i,j)

    return arr

arr = maldebrot(1, 1000)
plt.imshow(arr)
plt.show()
