# Lesson 4: Control Structures

Welcome to Lesson 4! In this lesson, we'll be learning about control structures, which allow us to control the flow of our code depending on certain conditions. We'll be focusing on `if`, `elif`, and `else` statements, which are the main types of control structures in Python.

## What are Control Structures?

In programming, control structures determine the flow of control (i.e., the order in which the program's code executes). They are a block of programming that analyzes variables and chooses a direction in which to go based on given parameters.

## If Statements

An `if` statement is the most simple form of control structure. It tests for a certain condition and executes the following code block if the condition is true. Here's an example:

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

In this code, Python will check if **'x'** is greater than 5. If this condition is true, it will print "x is greater than 5".

## Else Statements

An **'else'** statement follows an **'if'** or **'elif'** statement and executes when the condition in the **'if'** or **'elif'** statement is false. Here's an example:

```python
x = 2

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

```

In this code, since **'x'** is not greater than 5, Python will execute the code under the **'else'** statement.

## Elif Statements

The **'elif'** (short for 'else if') statement is a combination of **'else'** and **'if'**. It allows us to check for multiple conditions. If the condition for **'if'** is **'False'**, it checks the condition of the next **'elif'** block and so on. If all the conditions are **'False'**, the body of **'else'** is executed. Here's an example:

```python
x = 10

if x > 20:
    print("x is greater than 20")
elif x > 5:
    print("x is greater than 5 but not greater than 20")
else:
    print("x is not greater than 5")

```