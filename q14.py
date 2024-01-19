# 14.	Write a program that will check whether the number is armstrong number or not.
num = int(input("Enter the num: "))

sum = 0  # initilize the sum
order = len(str(num)) # getting the number of digit 
new_num = num  # copy the orginal numer as while running loop num is changing

while(num>0):
    digit = num%10  # to get last digit
    sum += digit ** order  # increment the sum variable
    num = num // 10  # reducing number 


if new_num == sum :
    print(f" the number {new_num} is an Armstrong number")
else: 
    print(f" the number {new_num} is not an Armstrong number")
