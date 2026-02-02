def generate_explanation(role, score, matched_skills, role_data):
    missing_skills = [
        skill for skill in role_data["skills"]
        if skill not in matched_skills
    ]

    explanation = f"{role} is suggested because your skills match {matched_skills}."

    next_steps = []
    for skill in missing_skills:
        next_steps.append(f"Improve {skill}")

    return {
        "reason": explanation,
        "missing_skills": missing_skills,
        "next_steps": next_steps
    }
