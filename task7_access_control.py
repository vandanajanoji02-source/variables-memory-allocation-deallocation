def check_access(age, has_id, is_employee):
    if (age >= 18 and has_id) or is_employee:
        return "Access granted"
    return "Access denied"


if __name__ == "__main__":
    print(check_access(20, True, False))