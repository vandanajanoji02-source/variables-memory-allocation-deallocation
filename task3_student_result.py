def get_result(marks):
    if marks >= 75:
        return "Distinction"
    if marks >= 35:
        return "Passed"
    return "Fail"


if __name__ == "__main__":
    print(get_result(82))