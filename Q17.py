__author__ = 'nayyarv'

units = "one two three four five six seven eight nine"
uniques = "ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
tens = "twenty thirty forty fifty sixty seventy eighty ninety"


unitsLen = len(units.replace(" ", ""))
uniquesLen = len(uniques.replace(" ", ""))
tensLen = len(tens.replace(" ", ""))

#sum to 99
sum99 = unitsLen + uniquesLen + tensLen*10 + 8*unitsLen

#sum to 999

sum999 = sum99 + ((len("hundred") + len("and"))*100 + sum99)*9 + (unitsLen *100)

print sum999#+ len("one") + len("thousand")