from Q1_30.Q9 import isPalindrome

__author__ = 'Varun Nayyar'
__date__ = "24/02/13 12:33 AM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."

if __name__ == "__main__":
    palSum = 0
    for i in xrange(int(1e6)):
        if isPalindrome(i) and isPalindrome(bin(i)[2:].lstrip("0")):
            print i, (bin(i)[2:].lstrip("0"))
            palSum += i

    print palSum