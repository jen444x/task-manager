def valid_day(day, month, year):
    """ Check if day is valid """

    # Used basic date check, will improve later with timetdate library
    
    """
    1. January (31 days)
    2. February (28 days in a common year and 29 days in leap years)
    3. March (31 days)
    4. April (30 days)
    5. May (31 days)
    6. June (30 days)
    7. July (31 days)
    8. August (31 days)
    9. September (30 days)
    10. October (31 days)
    11. November (30 days)
    12. December (31 days)
    """

    days_in_month = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:3,
        12:31
    }

    # Check if day is not in valid range
    if day > 0 and day < days_in_month[month]:
        return True

    """
    General rule: A year is a leap year if it is divisible by 4.
    Century year exception: A year divisible by 100 is not a leap year.
    Century year exception to the exception: A year divisible by 400 is a leap year. 
    """
    # check if it is a leap year for February
    if month == 2 and day == 29:
        if year % 4 == 0 and year % 100 != 0:
            return True
        if year % 400 == 0:
            return True
    
    # If none were true, not valid day
    return False

# Check if valid date format
def is_valid_date(date):
    date_list = date.split('/')

    # didnt use 2 / 
    if len(date_list) != 3:
        return False
    
    # Check vals are numbers
    for s in date_list:
        # make sure field is not empty
        if len(s) == 0:
            return False
        for c in s:
            if not c.isdigit():
                return False

    # turn each field into an int
    month, day, year = map(int, date_list)

    # Check month
    if month < 1 or month > 12:
        return False
    
    # Check day
    if not valid_day(day, month, year):
        return False
    
    # Check year
    if year < 2025:
        return False
    
    return True


# get due date
def get_user_due_date():
    """ Prompt user for due date"""

    due_date = input("Please enter due date (MM/DD/YYYY): ")

    valid_date = is_valid_date(due_date)

    while not valid_date:
        due_date = input("Due date was invalid. " \
        "Make sure to use the following format MM/DD/YY: ")

        valid_date = is_valid_date(due_date)
    
    return due_date



