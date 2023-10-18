name = input("Please enter your name: ")
print("Game#1")
game1_opponent = input("Name of opponent: ")
game1_yboxes = int(input("Number of boxes YOU created: "))
game1_oboxes = int(input("Number of boxes your OPPONENT created: "))
print("Game#2")
game2_opponent = input("Name of your opponent: ")
game2_yboxes = int(input("Number of boxes YOU created: "))
game2_oboxes = int(input("Number of boxes your OPPONENT created: "))
print("Game#3")
game3_opponent = input("Name of opponent: ")
game3_yboxes = int(input("Number of boxes YOU created: "))
game3_oboxes = int(input("Number of boxes your OPPONENT created: "))
print("Game#4")
game4_opponent = input("Name of opponent: ")
game4_yboxes = int(input("Number of boxes YOU created: "))
game4_oboxes = int(input("Number of boxes your OPPONENT created: "))
print("Game#5")
game5_opponent = input("Name of opponent: ")
game5_yboxes = int(input("Number of boxes YOU created: "))
game5_oboxes = int(input("Number of boxes your OPPONENT created: "))
print(" ")
total_points = game1_yboxes + game2_yboxes  + game3_yboxes + game4_yboxes + game5_yboxes
total_opponent_points = game1_oboxes + game2_oboxes + game3_oboxes + game4_oboxes + game5_oboxes
opp = "Opponent"
yp = "Your Points"
op = "Opponent Points"
box = "Box %"
game1_percent = game1_yboxes/49
game2_percent = game2_yboxes/49
game3_percent = game3_yboxes/49
game4_percent = game4_yboxes/49
game5_percent = game5_yboxes/49
print(f"Player's name: {name}")
print(" ")
print(" ")
print("Summary:")
print(f"Total points: {total_points}")
print(f"Total opponent points: {total_opponent_points}")
print(f"Percentage points received: {total_points/245:.2%}")
print(" ")
print("Dots and Boxes Score Tracker")
print(" ")
print(f"{opp}{yp:>16}{op:>20}{box:>10}")
print("-------------------------------------------------------")
print(f"{game1_opponent:<22}{game1_yboxes:<20}{game1_oboxes:<7}{game1_percent:.2%}")
print(f"{game2_opponent:<22}{game2_yboxes:<20}{game2_oboxes:<7}{game2_percent:.2%}")
print(f"{game3_opponent:<22}{game3_yboxes:<20}{game3_oboxes:<7}{game3_percent:.2%}")
print(f"{game4_opponent:<22}{game4_yboxes:<20}{game4_oboxes:<7}{game4_percent:.2%}")
print(f"{game5_opponent:<22}{game5_yboxes:<20}{game5_oboxes:<7}{game5_percent:.2%}")
print("-------------------------------------------------------")