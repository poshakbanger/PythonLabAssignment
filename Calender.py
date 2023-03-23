# Python program to display calendar of 2023
# given month of the year

# import module
import calendar

month = 1
while month < 13:
    print(calendar.month(2023, month))  # prints calendar of the month
    month += 1


def year():
    print(calendar.calendar(2023))  # prints all months of the year (in tabular form)


def month():
    print(calendar.month(2023, 2))  # prints the given month which is provided


def gap():
    print(calendar.month(2023, 2, 5))  # here 5 provides the space between dates