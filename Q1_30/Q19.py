__author__ = 'Varun Nayyar'
__date__ = "23/02/13 9:40 PM"
__copyright__ = "Company Confidential. Copyright (c) Cochlear Ltd 2012."

days = ["M", "Tu", 'W', 'TH', 'F', 'SA', 'SU'] #etc

months31 = [0, 2, 4, 6, 7, 9, 11]
months30 = [3, 5, 8, 10]


def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True


def numOfDays(month, year):
    if month in months31:
        return 31
    elif month in months30:
        return 30
    else:
        #February
        if isLeap(year):
            return 29
        else:
            return 28


def main():
    numSundays = 0
    startday = 1
    for year in range(1901, 2001):
        # print year

        for month in range(12):
            # print days[startday]
            if startday == 6:
                numSundays += 1
            startday = (startday + numOfDays(month, year)) % 7

    print numSundays


if __name__ == "__main__":
    main()
