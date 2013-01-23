__author__ = 'nayyarv'


ans = 2**1000


def digitSum(num):
    sum = 0
    while (num>=1):
        sum += num%10
        num/=10

    return sum


print digitSum(ans)
