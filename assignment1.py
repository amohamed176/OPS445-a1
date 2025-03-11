#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: "Umal Khayr Mohamed-amohamed176"
The python code in this file (assignment1.py) is original work written by
"Umal Khayr Mohamed-amohamed176". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, day: int) -> str:
    '''
    Based on the algorithm by Tomohiko Sakamoto
    Returns the day of the week as a three-letter abbreviation (e.g., 'mon', 'tue').
    '''
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def mon_max(month: int, year: int) -> int:
    '''
    Returns the maximum day for a given month and year.
    Handles leap years for February.
    '''
    if month == 2:
        return 29 if leap_year(year) else 28
    else:
        days_in_month = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        return days_in_month.get(month, 0)

def after(date: str) -> str:
    '''
    Returns the next day's date in YYYY-MM-DD format.
    Handles month and year transitions, including leap years.
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1

    max_day = mon_max(month, year)
    if tmp_day > max_day:
        to_day = 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1
        year += 1
    else:
        to_month = tmp_month

    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

def usage():
    '''
    Prints a usage message and exits the program.
    '''
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def leap_year(year: int) -> bool:
    '''
    Determines if a given year is a leap year.
    '''
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0

def valid_date(date: str) -> bool:
    '''
    Validates a date string in YYYY-MM-DD format.
    Checks for correct format and valid calendar date.
    '''
    parts = date.split('-')
    if len(parts) != 3:
        return False
    year_str, month_str, day_str = parts
    if len(year_str) != 4 or len(month_str) != 2 or len(day_str) != 2:
        return False
    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
    except ValueError:
        return False
    if month < 1 or month > 12:
        return False
    max_day = mon_max(month, year)
    if day < 1 or day > max_day:
        return False
    return True

def day_count(start_date: str, stop_date: str) -> int:
    '''
    Counts the number of weekend days (Saturdays and Sundays) between two dates.
    Iterates through each date from start_date to stop_date inclusive.
    '''
    start = min(start_date, stop_date)
    end = max(start_date, stop_date)
    count = 0
    current_date = start
    while current_date <= end:
        y, m, d = map(int, current_date.split('-'))
        dow = day_of_week(y, m, d)
        if dow in ['sat', 'sun']:
            count += 1
        current_date = after(current_date)
    return count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    date1 = sys.argv[1]
    date2 = sys.argv[2]
    if not valid_date(date1) or not valid_date(date2):
        usage()
    start, end = sorted([date1, date2])
    count = day_count(start, end)
    print(f"The period between {start} and {end} includes {count} weekend days.")





