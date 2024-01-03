def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True
    return False

def is_valid_date(year, month, day):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year):
        assert day <= days_leap_year[month-1], "Invalid Date"
    else:
        assert day <= days[month-1], "Invalid Date"

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    
    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though! 
    
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = min(year1, year2)
    days_l = 0
    for y in range(year, year1):
        if leap_year(y):
            days_l += 366
        else:
            days_l += 365
    if leap_year(year1):
        for month in range(month1 - 1):
            days_l += days_leap_year[month]
    else:
        for month in range(month1 - 1):
            days_l += days[month]
    days_l += day1
    
    days_h = 0
    for y in range(year, year2):
        if leap_year(y):
            days_h += 366
        else:
            days_h += 365
    if leap_year(year2):
        for month in range(month2 - 1):
            days_h += days_leap_year[month]
    else:
        for month in range(month2 - 1):
            days_h += days[month]
    days_h += day2
    assert(days_h >= days_l)
    return abs(days_h - days_l)

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    # test leap year difference
    assert(daysBetweenDates(2000, 1, 1,
                              2003, 3, 23)  == 1177)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()