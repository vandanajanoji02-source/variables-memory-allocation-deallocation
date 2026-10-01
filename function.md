# Python Functions

## 1. Why Use Functions?

Without a function, the same instructions may need to be repeated:

```python
print("Welcome, Vandana!")
print("Welcome, Pooja!")
print("Welcome, Roopa!")
```

A function lets us reuse the instructions with different values:

```python
def welcome(name):
    print("Welcome,", name)


welcome("Vandana")
welcome("Pooja")
welcome("Swati")
```

Functions help with code reuse, reduce repetition, improve organization, and make code easier to maintain and test.

## 2. What Is a Function?

A function is a reusable block of code that performs a specific task.

```python
def add(a, b):
    return a + b


total = add(2, 3)
print(total)  # 5
```

## 3. How Do You Define and Call a Function?

Defining a function gives it a name and describes what it will do. The body does not run until the function is called.

## 4. Does a Function Need Parameters?

A function does not need parameters if it always performs the same task.

```python
def welcome():
    print("Welcome to Nighan2 Labs!")


welcome()
```

## 5. What Are Function Parameters?

Parameters are the names listed in a function definition. Arguments are the values passed when calling the function.

```python
def welcome(name):
    print("Welcome,", name)


welcome("Vandana")
```

Here, `name` is a parameter and `"Vandana"` is an argument.

## 6. Can a Function Have Multiple Parameters?

A function can accept more than one parameter.

```python
def add(a, b):
    print(a + b)


add(10, 20)  # 30
```

## 7. How Does a Function Return a Value?

`print()` displays something. `return` sends a value back to the code that called the function, so it can be stored or used later.

```python
def add(a, b):
    return a + b


result = add(10, 20)
print(result)  # 30
```

## 8. What Happens After `return`?

`return` ends the current function call. Statements after it in the same function are not executed.

```python
def test():
    return 10
    print("This will not run")


print(test())  # 10
```

## 9. Can a Function Return Multiple Values?

Python can return several values. They are returned together as a tuple and can be unpacked into separate variables.

```python
def calculate(a, b):
    return a + b, a - b, a * b


sum_value, difference, product = calculate(10, 5)
print(sum_value)    # 15
print(difference)   # 5
print(product)      # 50
```

## 10. What Are Default Parameters?

A default parameter value is used when the caller does not provide an argument for that parameter.

```python
def greet(name="Vandana"):
    print("Hello,", name)


greet()           # Hello, Vandana
greet("Pooja")    # Hello, Pooja
```

Default parameters are useful when a value is common but callers should still be able to provide a different one.

## 11. How Are Positional Arguments Matched?

Positional arguments are matched to parameters by their order.

```python
def student(name, age):
    print(name, age)


student("Vandana", 20)
```

## 12. How Do Keyword Arguments Work?

Keyword arguments name the parameter they are assigned to, so their order does not matter.

```python
def student(name, age):
    print(name, age)


student(age=21, name="Vandana")
```

## 13. Can You Combine Positional and Keyword Arguments?

Positional arguments must come before keyword arguments in a function call.

```python
def student(name, age, course):
    print(name, age, course)


student("Vandana", 21, course="BCA")
student(name="Vandana", age=21, course="BCA")
```

The call `student(name="Vandana", 21, course="BCA")` is invalid because a positional argument follows a keyword argument.

## 14. What Is `*args`?

Use `*args` when a function should accept a variable number of positional arguments. Python collects them into a tuple.

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add(10, 20))           # 30
print(add(10, 20, 30))       # 60
print(add(1, 2, 3, 4, 5))    # 15
```

## 15. What Is `**kwargs`?

Use `**kwargs` when a function should accept a variable number of keyword arguments. Python collects them into a dictionary.

```python
def show_student(**details):
    print(details)


show_student(name="Vandana", age=21, course="BCA")
```

## 16. How Can You Combine Parameters, `*args`, and `**kwargs`?

Parameters can be combined in this order: regular parameters, `*args`, and `**kwargs`.

```python
def example(a, b=10, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)


example(1, 2, 3, 4, course="BCA")
```

## 17. What Is the Difference Between Local and Global Scope?

A local variable is created inside a function and is available there.

```python
def test():
    x = 10
    print(x)


test()
```

A function can read a global variable defined outside it.

```python
x = 100


def show_x():
    print(x)


show_x()  # 100
```

## 18. When Should You Use the `global` Keyword?

Use `global` to assign to a global variable from inside a function. Avoid global state when possible; parameters and return values usually make functions easier to reuse and test.

```python
count = 0


def increment():
    global count
    count += 1


increment()
print(count)  # 1
```

## 19. Can You Use a Local Variable Outside Its Function?

Trying to use a local variable outside the function where it was created raises a `NameError`.

```python
def test():
    x = 10


test()
print(x)  # NameError: x is not defined here
```

## 20. Can Functions Call Other Functions?

Functions can be composed into a sequence of steps. For example, one function can calculate a value and another can display it.

```python
def add(a, b):
    return a + b


def display():
    result = add(10, 20)
    print(result)


display()
```

A program's flow might look like this:

```text
main() -> validate() -> save() -> display()
```

## 21. What Is the Function-Calling Flow?

When a function is called, Python runs its body, returns the result, and assigns that result to the caller if requested.

```python
def multiply(a, b):
    return a * b


result = multiply(5, 4)
print(result)  # 20
```

Python calls `multiply` with `a = 5` and `b = 4`, calculates `5 * 4`, returns `20`, and stores it in `result`.

## 22. Are Functions Objects?

Functions are objects in Python. Assigning a function to another name does not call it; the new name refers to the same function object.

```python
def greet():
    print("Hello, world!")


x = greet
x()
```

Here, `x` refers to the `greet` function, and `x()` calls it.

## 23. Can You Pass a Function to Another Function?

Yes. A function that accepts or returns another function is called a higher-order function.

```python
def square(x):
    return x * x


def process(function, value):
    return function(value)


result = process(square, 5)
print(result)  # 25
```

`process` receives `square` as an argument and calls it with the value `5`.

## 24. What Are Lambda Functions?

A lambda is a small anonymous function, often used for a short operation.

```python
square = lambda x: x * x
print(square(5))  # 25
```

For example, `map` can apply a lambda to every item in a sequence:

```python
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)  # [2, 4, 6, 8]
```

## 25. What Is Recursion?

Recursion is when a function calls itself. A recursive function needs a base case that stops further calls.

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


countdown(5)
```

This prints `5` down to `1`, then stops when `n` reaches `0`.

## 26. How Do You Document a Function?

A docstring describes what a function does. It appears as the first statement in the function body and can be read through the `__doc__` attribute.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print(add.__doc__)
```

Writing clear docstrings is a useful professional Python habit.

## 27. What Are Type Hints?

Type hints communicate intended types to developers and tools. Python generally does not enforce them automatically at runtime.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Here, the hints indicate that `a` and `b` are expected to be integers and that the function is expected to return an integer.

## 28. How Can You Use a Function in a Practical Program?

This program calculates an electricity bill. It charges 2 per unit for the first 100 units, 4 per unit for the next 100, and 6 per unit for any additional units. It also adds a fixed charge of 100.

```python
def calculate_bill(units):
    if units <= 100:
        amount = units * 2
    elif units <= 200:
        amount = 100 * 2 + (units - 100) * 4
    else:
        amount = 100 * 2 + 100 * 4 + (units - 200) * 6
    return amount + 100


units = int(input("Enter units: "))
bill = calculate_bill(units)
print("Bill:", bill)
```

Why use `calculate_bill` instead of writing everything in the main program? Separating the calculation makes it easier to reuse, test, read, and maintain.

## 29. What Does a Good Function Generally Do?

A good function generally takes input, processes it, and produces an output.

```python
def calculate_area(length, width):
    return length * width


area = calculate_area(5, 3)
print(area)  # 15
```

## 30. Why Should You Avoid Giant Functions?

A giant function that handles validation, calculation, database work, and printing is difficult to understand and maintain. Prefer smaller functions with clear responsibilities.

```python
def get_student():
    ...


def validate_student(student):
    ...


def calculate_student_result(student):
    ...


def save_student_result(result):
    ...
```

This follows the single-responsibility principle: each function should have one clear job. Breaking work into smaller functions improves organization and maintainability; it does not necessarily make the program run faster.
