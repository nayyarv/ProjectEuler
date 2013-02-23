__author__ = 'Varun Nayyar'
__date__ = "24/02/13 12:14 AM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."


def sumOfDigitsToPowerOf(number, power):
    strNum = str(number)
    sumDigitpower = 0
    for digit in strNum:
        sumDigitpower += int(digit) ** power
        # print sumDigitpower
    return sumDigitpower


specialSum = 0
for i in xrange(10, int(1e6)):
    if sumOfDigitsToPowerOf(i, 5) == i:
        print i
        specialSum += i

print specialSum

