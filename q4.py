# 4.	Write a program that will give you the sum of 3 digits
digit1 = int(input("Enter the first digit: "))
digit2 = int(input("Enter the second digit: "))
digit3 = int(input("Enter the third digit: "))

sum = digit1 + digit2 + digit3
print("The sum of three digit's are: ",sum)

# sum of a three digit number
number = int(input("Enter any three digit number:"))

digit01 = number//100
digit02 = (number//10)%10
digit03 = (number%10)
sum2 = digit01 + digit02 + digit03
print("the sum of given three digit number is:",sum2)