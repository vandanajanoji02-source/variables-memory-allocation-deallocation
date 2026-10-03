def validate_login(username, password):
    if username == "Admin" and password == "python123":
        return "Valid user"
    return "Invalid user"


if __name__ == "__main__":
    print(validate_login("Admin", "python123"))