def multiply(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x * y 
    else:
        return "Please enter two numbers."
      
num1 = 4
num2 = 5
print(f"{multiply(num1, num2)}")