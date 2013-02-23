__author__ = 'Varun Nayyar'
__date__ = "22/02/13 7:10 PM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."


def sumOfDivisors(number):
    count = 2
    sum = 1
    while (count**2 <= number):
        if number%count ==0:
            sum+=(count+number/count)
        count+=1
    if (count-1)**2 == number:
        sum-=count #don't count twice
    return sum

if __name__ == "__main__":
    seenNums = set([])
    amicables = set([])

    for num in range(10001):
        if num in seenNums or num in amicables: continue
        d_num = sumOfDivisors(num)
        if sumOfDivisors(d_num) == num and num!=d_num:
            #we have an amicable pair

            amicables.add(d_num)
            amicables.add(num)
        else:
            seenNums.add(d_num)
            seenNums.add(num)

    print amicables
    print sum(amicables)


