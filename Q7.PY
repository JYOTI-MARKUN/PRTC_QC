# 7.	Write a program that will tell whether the given year is a leap year or not.
year = int(input("Enter the year: "))

if year % 4 ==0:
    if year % 100 ==0:
        if year %400 ==0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")                    


# another approach
year1 = int(input("Enter the Year: "))    

if (year1 % 4 == 0 and year1 % 100 != 0) or (year % 400 == 0):
    print("it's a leap year")
else:
    print("It's not a leap year")    
    

