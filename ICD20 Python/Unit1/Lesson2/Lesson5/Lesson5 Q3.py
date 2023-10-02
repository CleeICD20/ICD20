distance_input = (float(input("What is the distance of your trip (km): ")))
fuel_efficiency_input = (float(input("What is the fuel efficiency of your vehicle written in the # of kilometers per liter: ")))
price_input = (float(input("What is the current price of fuel per liter: ")))
passengers_input = (float(input("How many passengers are in the vehicle: ")))
fuel_needed = distance_input/fuel_efficiency_input
fuel_cost = fuel_needed * price_input
fuel_cost_per_passenger = fuel_cost/passengers_input
print(f"You will need {fuel_needed}L for the distance of this trip.")
print(f"The total cost of fuel for this trip will be ${fuel_cost}")
print(f"The cost of fuel per passenger if you split it evenly among each of you will be ${fuel_cost_per_passenger}")