def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    if operator == "//":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a // b
    if operator == "%":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a % b
    if operator == "**":
        return a ** b
    raise ValueError("Invalid operator")


if __name__ == "__main__":
    print(calculate(2, "**", 3))