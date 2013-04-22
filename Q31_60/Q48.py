__author__ = 'nayyarv'

sum = 0
for i in range(1000):
    i += 1
    sum = (sum + i ** i) % (10 ** 10)

print sum