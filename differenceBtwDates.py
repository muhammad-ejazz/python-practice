#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates.
#

from math import floor


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if month2 in [1, 2]:
        month2 += 12
        year2 -= 1
    if month1 in [1, 2]:
        month1 += 12
        year1 -= 1
    days2 = 365 * year2 + floor(year2/4) - floor(year2/100) + floor(year2/400) + day2 + floor((153*month2+8)/5)
    days1 = 365 * year1 + floor(year1/4) - floor(year1/100) + floor(year1/400) + day1 + floor((153*month1+8)/5)
    days = days2 - days1
    return days

# Test routine


def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed", answer, result)
        else:
            print ("Test case passed!")


test()