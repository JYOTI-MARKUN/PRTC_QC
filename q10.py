# 10.	Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
cost_price = float(input("Enter the cost price: "))
sell_price = float(input("Enter the sell price: "))


if cost_price > sell_price :
    print("It's a loss")
elif cost_price == sell_price:
    print("It's neither loss nor profit")
else:
    print("It's a profit")
        
     