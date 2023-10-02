price1 = (float(input("What was the cost of your first item: ")))
price2 = (float(input("What was the cost of your second item: ")))
price3 = (float(input("What was the cost of your third item: ")))
Total = price1 + price2 + price3 
tax = (price1 + price2 + price3) * 1.08
print(f"Item 1 cost: ${price1}")
print(f"Item 2 cost: ${price2}")
print(f"Item 3 cost: ${price3}")
print(f"Total Cost: {Total}")
print(f"Sales Tax Total Cost: {tax}")