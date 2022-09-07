# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
# if year is equal or smaller than 1580 it is "Not within the Gregorian calendar period"

year = int(input("Enter a year: "))

if year>1580:
    if (year%4)!=0:
        print("common year")
    elif (year%100)!=0:
        print("leap year")
    elif (year%400)!=0:
       print("common year")
    else:
       print("leap year")
else:
    print("Not within the Gregorian calendar period")
