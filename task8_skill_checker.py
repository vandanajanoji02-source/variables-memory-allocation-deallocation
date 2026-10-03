required_skills = ["python", "SQL", "Git", "HTML"]


def check_skill(skill_name):
    if skill_name in required_skills:
        return "Skill available"
    return "Skill not available"


if __name__ == "__main__":
    print(check_skill("python"))