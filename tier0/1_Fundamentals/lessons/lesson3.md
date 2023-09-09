# Lesson 3: Loops

Welcome to Lesson 3! In this lesson, we'll be covering one of the fundamental building blocks of programming: loops. Loops are incredibly powerful and allow us to automate repetitive tasks, making our code more efficient and easier to manage.

## What are loops?

In programming, a loop is a sequence of instructions that is continually repeated until a certain condition is met. We use loops when we want to repeat a specific block of code an unknown number of times until a certain condition is met. 

## Types of loops

There are several types of loops, but we'll be covering two main types in this lesson:

1. **For loop**: A `for` loop is used for iterating over a sequence like a list, tuple, dictionary, string, or array. It's like saying, "for each element in this sequence, perform this action". Here's a basic example:

```python
for i in range(5):
    print(i)
```

This code will print the numbers 0 through 4. The **'range(5)'** part generates a sequence of numbers from 0 to 4, and the **'for'** 8 loop iterates over this sequence.

1. **While loop**: A **'while'** loop continues to execute the code block as long as the given condition is **'True'**. It's like saying, "while this condition holds, keep performing this action". Here's a simple example:

```python
i = 0
while i < 5:
    print(i)
    i += 1

```

This code will output the same result as the **'for'** loop above. The loop will keep iterating as long as **'i'** is less than 5.

## Loop control statements

Loop control statements change the execution from its normal sequence. The main control statements are **break**, **continue**, and **pass**.

- **break**: Terminates the loop and transfers execution to the statement immediately following the loop.
- **continue**: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
- **pass**: The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.