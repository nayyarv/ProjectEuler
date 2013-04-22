__author__ = 'Varun Nayyar'
__date__ = "22/04/13 6:01 PM"


def treeTraverser():
    f = open("../Data/q67triangle.txt")
    maxSums = map(int, f.readline().split())
    for lines in f:
        nums = map(int, lines.split())

        newMax = list(maxSums)

        for i in range(1, len(maxSums)):
            newMax[i] = nums[i] + max(maxSums[i], maxSums[i - 1])

        newMax.append(maxSums[-1] + nums[-1])
        newMax[0] = nums[0] + maxSums[0]

        maxSums = newMax

    f.close()

    return max(maxSums)


if __name__ == "__main__":
    print treeTraverser()
