#1.	User will input (3ages).Find the oldest one
age1 = int(input("Enter first Age"))
age2 = int(input("Enter Second Age"))
age3 = int(input("Enter Third Age"))


if age1 > age2 and age1 > age3 :
    print(f"The oldest one is:",age1) 
elif age2 > age1 and age2 > age3 :
    print(f"The oldest one is:",age2)
else:
    print(f"The oldest one is:",age3)    

