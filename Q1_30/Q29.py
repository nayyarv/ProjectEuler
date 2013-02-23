__author__ = 'Varun Nayyar'
__date__ = "24/02/13 12:25 AM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."

maxA = 100
maxB = 100
distinctPowers = set([])

for a in range(2, maxA + 1):
    for b in range(2, maxB + 1):
        distinctPowers.add(a ** b)

print len(distinctPowers)
print distinctPowers