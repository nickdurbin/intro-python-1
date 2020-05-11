"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

inputLength = len(sys.argv)
print(len(sys.argv))
date = datetime.now()
print(date)

def number_of_args(num):
  return int(sys.argv[num])

if inputLength == 1: # If no input prints the calendar
  date = date
elif inputLength == 2: # If passed the month prints the calendar for that month and this year.
  date = datetime(date.year, number_of_args(1), 1)
elif inputLength == 3:
  date = datetime(number_of_args(1), number_of_args(2), 1)
else:
  print("Please enter month and year in the following format: `py -m 14_cal [month e.g. 1-12] [year e.g 1900]`")
  sys.exit()

print(calendar.month(date.year, date.month))