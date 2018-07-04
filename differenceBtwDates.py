#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates.
#
from datetime import  date


def is_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    #d1 = date(year2, month2, day2)
    #d2 = date(year1, month1, day1)
    #return (d1 - d2).days
    if is_leap(year1):
        day1 += 1
    if is_leap(year2):
        day2 += 1
    if day2 < day1:
        day2 += 30
        month2 -= 1
    days = day2 - day1
    if month2 < month1:
        month2 += 12
        year2 -= 1
    days += (month2 - month1) * 30
    days += (year2 - year1) * 365
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