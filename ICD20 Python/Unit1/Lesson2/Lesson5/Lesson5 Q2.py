wall_length = (float(input("Enter the length of one wall: ")))
wall_width = (float(input("Enter the width of one wall: ")))
house_height = (float(input("Enter the height of the house: ")))
brick_cost = (float(input("Enter the cost of one brick: ")))
brick_length = (float(input("Enter the length of a standard brick: ")))
brick_width = (float(input("Enter the width of a standard brick: ")))
brick_height = (float(input("Enter the hieght of a standard brick: ")))
long_side_wall = wall_length * house_height * 2 
wide_side_wall = wall_width * house_height * 2
top = wall_length * wall_width
surface_area = long_side_wall + wide_side_wall + top
long_side_brick = brick_length * brick_height * 2
wide_side_brick = brick_width * brick_height * 2 
brick_top = brick_length * brick_width * 2
brick_surface_area = long_side_brick + wide_side_brick + brick_top
bricks_required = surface_area/brick_surface_area
brick_cost = bricks_required * brick_cost 
print("House Details:")
print(f"- Surface area of walls and top: {surface_area} square meters")
print(f"- Bricks required: {bricks_required} bricks")
print(f"- Total cost of bricks: ${brick_cost}")