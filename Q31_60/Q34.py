from math import factorial

__author__ = 'Varun Nayyar'
__date__ = "24/02/13 12:28 AM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."


def digitFactorial(number):
    strNum = str(number)
    sumDigitFactorial = 0
    for digit in strNum:
        sumDigitFactorial += factorial(int(digit))
    return sumDigitFactorial


specialSum = 0
for i in xrange(10, int(1e6)):
    if digitFactorial(i) == i:
        print i
        specialSum += i

print specialSum




