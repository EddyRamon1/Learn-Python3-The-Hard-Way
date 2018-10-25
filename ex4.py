# The integers here are assigned to the numbers given in this excercise. In this case for line 1, I assign the variable car to an integer of 100.
cars = 100

# The "space_in_a_car" variable is assigned to 4.0
space_in_a_car = 4.0

# The "drivers" variable is assigned to 30
drivers = 30

# The "passemgers" variable is assigned to 90
passengers = 90

# The "cars_not_driven" variable is assigned to previous variables that were already assigned (cars and drivers), and subtracts them.
cars_not_driven = cars - drivers

# The "cars_driven" variable is assigned to a previous variable that was already assigned (drivers).
cars_driven = drivers

# The "carpool_capacity" variable is assinged to previous variables that were already assigned (cars_driven and space_in_a_car), and multiplies them.
carpool_capacity = cars_driven * space_in_a_car

# The "average_passengers_per_car is assigned to previous variables that were already assigned (passengers and cars_driven), and divides them.
average_passengers_per_car = passengers / cars_driven


# It prints out the statement and the integer will display its assigned number
print("There are", cars, "cars available.")

# It prints out the statement and the integer will display its assigned number
print("There are only", drivers, "drivers available.")

# It prints out the statement and the inetger will display its assigned calculation
print("There will be", cars_not_driven, "empty cars today.")

# It prints out the statement and the integer will display its assigned calculation
print("We can transport", carpool_capacity, "people today.")

# It prints out the statement and the integer will display its assigned number
print("We have", passengers, "to carpool today.")

# It prints out the statement and the integer will display its assigned calculation
print("We need to put about", average_passengers_per_car, "in each car.")
