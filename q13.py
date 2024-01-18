# 13.	Write  a program that will tell whether the given number is divisible by 3 & 6.
def divisible(num):
    if num % 3 == 0 and num % 6 == 0:
        print("The given number is divisible by 3 and 6")
    else:
        print("The num is not divisible by 3 and 6")


num = int(input("Enter the number: "))
result = divisible(num)


