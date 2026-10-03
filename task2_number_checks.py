def check_number(number):
    return {
        "even": number % 2 == 0,
        "odd": number % 2 != 0,
        "divisible by 3": number % 3 == 0,
        "divisible by 5": number % 5 == 0,
    }


if __name__ == "__main__":
    print(check_number(15))