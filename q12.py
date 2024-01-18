# 12.	Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
import math
def volume_of_cylinder(radius,height):
    volumn = math.pi * radius * radius * height
    return volumn

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

result = round(volume_of_cylinder(radius,height),2)
print("The volume of the cylinder is:",result)