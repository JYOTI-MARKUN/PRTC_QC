# 17.	Write a program that will take three digits from the user and add the square of each digit.
def add_square(num1,num2,num3):
    addsquare = num1**2 +num2**2+num3**2
    return addsquare

digit1 = int(input("Enter the first Digit: "))
digit2 = int(input("Enter the second Digit: "))
digit3 = int(input("Enter the third Digit: "))


square = add_square(digit1,digit2,digit3)
print(square)