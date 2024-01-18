# 9.	Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
angle1 = int(input("Enter the value of first angle: "))
angle2 = int(input("Enter the value of second angle: "))
angle3 = int(input("Enter the value of third angle: "))

sum = angle1 + angle2 + angle3

if sum == 180 :
    print("The sum of the angles provided by you is 180 so it forms a triangle")

else:
    print("The sum of the angles provided by you is not 180 so it doesn't forms a triangle")    




