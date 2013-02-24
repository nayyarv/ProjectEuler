__author__ = 'nayyarv'

highestPalindrome = 10001


def isPalindrome(num):
    test = repr(num)
    return test == test[::-1]


#for number in range(1000*1000, (100*100-1), -1):
#    if isPalindrome(number):

if __name__ == "__main__":
    for num1 in range(999, 99, -1):
        for num2 in range(999, 99, -1):
            prod = num1 * num2
            if prod <= highestPalindrome:
                continue
            else:
                if isPalindrome(prod):
                    print num1, num2, prod
                    highestPalindrome = prod

    print highestPalindrome

