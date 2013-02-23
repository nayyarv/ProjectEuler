__author__ = 'nayyarv'

f = open("../Data/names.txt")
names = f.next()

names = names.split(',')
names = sorted(names)

CumulativeNameScore = 0

for i in range(len(names)):
    name = names[i].strip('"')
    # print name
    score = (i + 1) * sum(map(lambda x: ord(x) - 64, name))
    CumulativeNameScore += score
    # print name, score

print CumulativeNameScore
