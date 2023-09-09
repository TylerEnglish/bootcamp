# 1. Using a for loop and the range function, print the numbers 0 to 10

for i in range(11):
    print(i)

# 2. Using a while loop, print the numbers 0 to 10

i = 0
while i < 11:
    print(i)
    i += 1

# 3. Write a for loop that iterates over a list of names and prints each one

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

for name in names:
    print(name)

# 4. Use a break statement in a loop to print the numbers 1-5 only

for i in range(1, 11):
    if i > 5:
        break
    print(i)

# 5. Use a continue statement in a loop to print the odd numbers between 1 and 10

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
