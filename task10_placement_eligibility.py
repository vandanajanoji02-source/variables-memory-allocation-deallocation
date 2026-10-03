def check_placement_eligibility(age, marks, attendance, experience, has_backlog):
    eligible = marks >= 60 and attendance >= 75 and not has_backlog

    experience_level = str(experience).strip().lower()
    if experience_level == "0":
        category = "Fresher"
    elif experience_level == "1-2":
        category = "Junior"
    elif experience_level == "more than 2":
        category = "Experienced"
    else:
        raise ValueError("Experience must be '0', '1-2', or 'more than 2'")

    return eligible, category


if __name__ == "__main__":
    placement_eligible, candidate_category = check_placement_eligibility(
        21, 72, 80, "1-2", False
    )
    print("Placement eligible:", "Yes" if placement_eligible else "No")
    print("Candidate category:", candidate_category)