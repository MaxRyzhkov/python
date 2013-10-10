import random
import matplotlib.pyplot as plt


def coin():
    v = random.random()
    if v < 0.5: return 0
    else: return 1

def experiment(n):
    xs = []
    for a in range(n): xs.append(coin())
    return xs

def ones(xs):
    acc = 0
    for a in xs:
        if a == 1: acc = acc+1
    return acc

myExp = []
for a in range(1000):
    xs = experiment(100)
    v = ones(xs)
    myExp.append(v)


# the histogram of the data
(ys, xs, q) = plt.hist(myExp)
plt.plot(ys, '-r')
plt.show()
