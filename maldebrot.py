from numpy import *
import matplotlib.pyplot as plt

def maldebrot(size, nmax):
    counter = [0]
    def ijC(i,j):
        k = float(size) / (nmax-1)
        x = 2*k*i - size
        y = 2*k*j - size
        z = x + 1j*y
        return z

    def colorize(i,j):
        z = ijC(i,j)
        color = 0
        c = z
        while (abs(z) < 2 and color < 256):
            counter[0] = counter[0] + 1
            z = z*z + c
            color += 1
        return color

    arr = zeros((nmax,nmax))
    for i in range(nmax):
        print (100.0*i/nmax)
        for j in range(nmax):
            arr[i][j] = colorize(i,j)

    print counter
    return arr

arr = maldebrot(1, 1000)
plt.imshow(arr)
plt.show()
