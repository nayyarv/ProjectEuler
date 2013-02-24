__author__ = 'Varun Nayyar'
__date__ = "24/02/13 4:17 PM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."


def digit(position):
    numInSet = 9
    numDigits = 1
    currentPos = 1
    while (position >= currentPos):
        if position >= (currentPos + numInSet * numDigits):
            currentPos += (numInSet * numDigits)
            numInSet *= 10
            numDigits += 1
        else:
            # print currentPos
            relativePos = position - currentPos
            rDiv, rMod = divmod(relativePos, numDigits)
            baseNum = 10 ** (numDigits - 1)
            baseNum += rDiv
            return nthdigitof(baseNum, rMod)

            #within level
            #at this section - we are at the start of new sequenc i.e. 100 with 3 digits, 1000, with 9 digits


def nthdigitof(number, n):
    return int(str(number)[n])


def main():
    for i in range(5, 20):
        print digit(i),
    res = 1
    for i in range(7):
        res *= digit(10 ** i)

    print res


if __name__ == "__main__":
    main()