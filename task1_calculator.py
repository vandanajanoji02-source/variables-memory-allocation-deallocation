def calculate(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b,
        "floor division": a // b,
        "remainder": a % b,
    }


if __name__ == "__main__":
    print(calculate(10, 3))