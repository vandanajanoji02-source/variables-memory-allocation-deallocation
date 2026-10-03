def check_eligibility(marks, attendance_percentage, has_backlog):
    if marks >= 60 and attendance_percentage >= 75 and not has_backlog:
        return "Eligible"
    return "Not eligible"


if __name__ == "__main__":
    print(check_eligibility(72, 80, False))