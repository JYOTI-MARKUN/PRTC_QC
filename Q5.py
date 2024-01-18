# 5.	Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
num = int(input("Enter any three digit number:"))
reverse_num =int(str(num)[::-1])
print("The reverse number of the given number is: ",reverse_num)

# note in the above [::-1] is list or string slicing which indicates start , end and swap value if any value is ommited the default value is start for beginning end for stop 