# Exercise 1:
print("-----Exercise 1-----")
# Personal information
my_name = "Alice"
my_age = 25
my_height = 170
my_weight = 70

# Form a sentence and print
sentence = f"My name is {my_name}, I am {my_age} years old, {my_height} cm tall, and weigh {my_weight} kg."
print(sentence)

# Exercise 2:
print("\n-----Exercise 2-----")
# Store item information
price_per_item = 50
num_items = 5

# Calculate the total cost
total_cost = price_per_item * num_items

# Print out the total cost
print(f"The total cost of your {num_items} items is: ${total_cost}.")

# Exercise 3:
print("\n-----Exercise 3-----")
# Rectangle dimensions
rectangle_width = 10
rectangle_height = 20

# Calculate the area
rectangle_area = rectangle_width * rectangle_height

# Print out the area
print(f"The area of the rectangle with width {rectangle_width} and height {rectangle_height} is: {rectangle_area} sq units.")

# Exercise 4: 
print("\n-----Exercise 4-----")
# Swapping values
first_value = 5
second_value = 10

# Print initial values
print(f"Initial values: first_value = {first_value}, second_value = {second_value}")

# Swap values
first_value, second_value = second_value, first_value

# Print after swap
print(f"Values after swap: first_value = {first_value}, second_value = {second_value}")

# Exercise 5: 
print("\n-----Exercise 5-----")
# Temperature conversion
temp_in_fahrenheit = 77

# Convert to Celsius
temp_in_celsius = (temp_in_fahrenheit - 32) * 5/9

# Print out the result
print(f"{temp_in_fahrenheit} degrees Fahrenheit is equal to {round(temp_in_celsius, 2)} degrees Celsius.")
