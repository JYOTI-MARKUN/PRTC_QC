# 8.	Write a program to find the euclidean distance between two coordinates.
import math

x1 = int(input("Enter the x coordinate of first number: "))
x2 = int(input("Enter the x coordinate of second number: "))
y1 = int(input("Enter the y coordinate of first number: "))
y2 = int(input("Enter the y coordinate of second number: "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("The Euclidean distance between two number is",distance)