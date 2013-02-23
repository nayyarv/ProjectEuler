__author__ = 'nayyarv'


def Collatz(num):
    if num % 2 == 0: #is even
        return num / 2
    else:
        return (3 * num) + 1


import numpy as np

lookup = np.zeros(10000)

maxChainLen = 0
maxChainNum = 0

lookup[0] = 0
lookup[1] = 0

for i in range(2, 10000):
    chainLen = 0
    num = Collatz(i)
    while (num > 1):
        num = Collatz(num)
        chainLen += 1

    lookup[i] = chainLen

for i in range((10 ** 6) - 1, 10000 - 1, -1):
    chainLen = 0
    num = Collatz(i)
    while (num >= 10000):
        num = Collatz(num)
        chainLen += 1

    chainLen += lookup[num]

    if chainLen > maxChainLen:
        maxChainLen = chainLen
        maxChainNum = i
        print (i, chainLen)

print (maxChainNum, maxChainLen)
