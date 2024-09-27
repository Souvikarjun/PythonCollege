import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

print("\nHere is the calendar for the given month and year:\n")
print(calendar.month(year, month))