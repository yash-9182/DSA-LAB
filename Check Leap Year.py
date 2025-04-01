def is_leap_year(year):
    print("Checking if", year, "is a leap year")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
year = 2024
print("Is Leap Year:", is_leap_year(year))
print("---------------------------")
