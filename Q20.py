__author__ = 'nayyarv'



def digitSum(num):
    sum = 0
    while (num>=1):
        sum += num%10
        num/=10

    return sum

def factorial(n):
    if n >1:
        return n * factorial(n-1)
    else:
        return 1



print digitSum(factorial(100))