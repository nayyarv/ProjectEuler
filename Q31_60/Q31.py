__author__ = 'Varun Nayyar'
__date__ = "24/02/13 4:04 PM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."

denominations = [1, 2, 5, 10, 20, 50, 100, 200]


def main():
    print numberOfways(200, 200) #ans = 73682


def numberOfways(amount, maxDenomination):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    else:
        numWays = 0
        for i in denominations:
            if i > maxDenomination:
                break
            else:
                numWays += numberOfways(amount - i, i)
        return numWays


if __name__ == "__main__":
    main()