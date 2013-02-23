from math import factorial

__author__ = 'Varun Nayyar'
__date__ = "23/02/13 10:24 PM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."


def factorialBuilder(maxInt):
    factDict = {0: 1}
    for i in range(1, maxInt + 1):
        factDict[i] = factorial(i)

    return factDict


def main():
    FactDict = factorialBuilder(9)
    numberSet = (range(0, 10))
    ans = ""
    target = 1e6 - 1

    for i in range(9, 0, -1):
        currentFact = FactDict[i]
        print target, i

        for j in range(len(numberSet) + 1):
            if target == 0:
                print ans, numberSet, len(ans)
                return
            elif j * currentFact > target:
                target -= (j - 1) * currentFact
                print j - 1, numberSet[j - 1]
                ans += str(numberSet[j - 1])
                numberSet.remove(numberSet[j - 1])
                break
        if len(numberSet) == i + 1:
            #append last one onto the number
            print "reached end"
            pass

    print ans, numberSet, len(ans)


if __name__ == "__main__":
    main()
