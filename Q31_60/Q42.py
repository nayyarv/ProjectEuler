__author__ = 'Varun Nayyar'

import numpy as np
from matplotlib import pyplot as plt


def triangleNums(maxVal):

    index = 0.5*(-1+np.sqrt(1+8*maxVal))
    # print int(index)+1
    nums = np.arange(1, int(index)+2)
    tris = nums.cumsum()
    return tris


def main():
    names = nameReader()
    vals = namesToNums(names)
    print max(vals)
    tris = triangleNums(max(vals))

    count = 0

    for number in vals:
        if number in tris:
            count+=1

    print count

def nameReader():
    with open("../Data/p042_words.txt") as f:
        nameline = f.readline()
        names = nameline.split('","')
        names[0]= names[0].lstrip('"')
        names[-1]= names[-1].rstrip('"')
    return names


def namesToNums(nameslist):
    vals = np.zeros(len(nameslist))
    i=0
    for name in nameslist:
        total = 0
        for letter in name:
            total+= ord(letter)-ord("A")+1

        vals[i] = total
        i+=1
    return vals

def isTriangle(num):
    pass



if __name__ == "__main__":
    main()