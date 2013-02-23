__author__ = 'Varun Nayyar'
__date__ = "23/02/13 10:18 PM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."


def Spiral(gridSize):
    assert gridSize % 2 == 1

    diagSum = 1
    currentElement = 1
    stepSize = 2
    while (stepSize - 1 != gridSize):
        for i in range(4):
            currentElement += stepSize
            diagSum += currentElement
        stepSize += 2

    return diagSum


print Spiral(1001)
