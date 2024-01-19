# 20.	Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).

# def in_hand_salary(salary):

#     hra = 0.1 * salary
#     net_salary = salary - hra

#     da = 0.05 * salary
#     net_salary -= da

#     pf = 0.03 * salary
#     net_salary -= pf

#     if  0 < salary <100000 :
#         tax = 0

#     elif 100000 <= salary <500000 :
#         tax = 0.1* salary
    
#     elif 500000 <= salary <1000000 :
#         tax = 0.2* salary
      
#     else:
#         tax = 0.3* salary

#     net_salary -= tax

#     return net_salary


# salary = int(input("Enter your salary: "))

# gross_salary = in_hand_salary(salary)

# print("Your in hand salary is ",gross_salary)


salary = int(input("Enter the salary: "))  

if 0 < salary < 100000 :
    net_salary = salary - (salary * 0.1 + salary * 0.05 + salary * 0.03)         

elif 100000 <= salary < 500000 :
    net_salary = salary - (salary * 0.1 + salary * 0.05 + salary * 0.03) - salary * 0.1  

elif 500000 <= salary < 1000000 :
    net_salary = salary - (salary * 0.1 + salary * 0.05 + salary * 0.03) - salary * 0.2   

else:
    net_salary = salary - (salary * 0.1 + salary * 0.05 + salary * 0.03) - salary * 0.3         


print(f"Your in hand salary will be {net_salary}")