# 15.	Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.
num = int(input("Enter a four digit number: "))

sum = 0
new_num = num
order = len(str(num))

while(num>0):
    digit = num %10
    sum += digit ** order
    num = num // 10

if new_num == sum :
    print(f"The given four digit number {new_num} is an Armstrong number")    
else:
    print(f"The given four digit number {new_num} is not an Armstrong number")       
