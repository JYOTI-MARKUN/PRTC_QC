# 3.	User will input (2numbers).Write a program to swap the numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
temp = num1
num1 = num2
num2 = temp

print("The first, second number after swaping is:",num1,num2)

# alternate solution
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("The first, second number after swapping is:", num1, num2)
