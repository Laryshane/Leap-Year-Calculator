# Use this Code to determine a leap year

year = int(input("Enter a year: "))

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
# Year cannot be less that 1582 since that is when the Gregorian Calendar was created.
if year < 1582:
    print("Not within the Gregorian calendar period.")
elif year % 4 != float():
    print("Common Year")
elif year % 100 != float():
    print("Leap Year")
elif year % 400 != float():
    print("Common Year")
else:
    print("Leap Year")
