def score_user_for_role(user, role_data):
    score = 0
    matched_skills = []

    for skill in role_data["skills"]:
        if skill in user["skills"]:
            score += 20
            matched_skills.append(skill)

    for interest in role_data["interests"]:
        if interest in user["interests"]:
            score += 15

    for strength in role_data["strengths"]:
        if strength in user["strengths"]:
            score += 10

    return score, matched_skills
