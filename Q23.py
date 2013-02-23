__author__ = 'Varun Nayyar'
__date__ = "22/02/13 7:52 PM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."

from numpy import array

from Q21 import sumOfDivisors


def isAbundant(number):
    divSum = sumOfDivisors(number)
    # print  number, divSum
    if divSum > number:
        return True
    else:
        return False


def canBeExpressedAsSumof2(number, sortedArray):
    i = 0
    while sortedArray[i] * 2 <= number:
        diff = number - sortedArray[i]
        if diff in sortedArray:
            return True
        i += 1
    return False


def main():
    Abundants = []
    for i in range(2, 28123):
        if isAbundant(i):
            Abundants.append(i)
    print Abundants[:12]
    Abundants = array(Abundants)

    sumValues = 0
    for i in range(5000):
        if not canBeExpressedAsSumof2(i, Abundants):
            print i
            sumValues += i

    print sumValues


if __name__ == "__main__":
    main()




