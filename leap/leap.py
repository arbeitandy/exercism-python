def is_leap_year(year):
    try:
        if year % 400  == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
    except:
        return False
    