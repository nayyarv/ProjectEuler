__author__ = 'nayyarv'

curr = 1
prev = 1
index = 2

while (len(repr(curr)) != 1001):
    temp = curr
    curr += prev
    prev = temp
    index += 1

    print (index, curr)

print curr
print index


