# 11.	Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
principle = int(input("Enter the principle amount: "))
roi = int(input("Enter the rate of interest: "))
time = int(input("Enter the time period in years: "))

SI = (principle * roi * time ) / 100
SI = print("The simple interest is",SI)