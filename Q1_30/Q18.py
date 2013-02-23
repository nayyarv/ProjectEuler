__author__ = 'Varun Nayyar'
__date__ = "22/02/13 7:23 PM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."


def pathMaximizer(rowNum, columnNum):
    global Numbers
    if rowNum == len(Numbers) - 1:
        #last row
        return Numbers[rowNum][columnNum]

    else:
        #within bounds
        try:
            return Numbers[rowNum][columnNum] + max(pathMaximizer(rowNum + 1, columnNum),
                                                    pathMaximizer(rowNum + 1, columnNum + 1))
        except IndexError as e:

            print "Something weird"
            raise


if __name__ == "__main__":
    global Numbers
    Numbers = []
    with open("../Data/q18Triangle.txt") as f:
        for line in f:
            nums = line.split()
            nums = map(int, nums)
            Numbers.append(nums)

    print pathMaximizer(0, 0)






