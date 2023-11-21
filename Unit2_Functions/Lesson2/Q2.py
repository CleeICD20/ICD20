import math 
def calculate_cylinder_volume(radius, height):
    if isinstance(radius, (int, float)) and isinstance(height, (int, float)):
        return math.pi * radius ** 2 * height
    else:
        return "Please enter two numbers"
    

print(f"{calculate_cylinder_volume(4, 9)}")
