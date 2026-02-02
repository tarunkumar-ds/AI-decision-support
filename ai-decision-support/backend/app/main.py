from fastapi import FastAPI
from app.schemas import UserProfile
from app.rules.career_rules import CAREER_ROLES
from app.engine.scorer import score_user_for_role
from app.engine.explainer import generate_explanation
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Career Decision Support System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/recommend-career")
def recommend_career(user: UserProfile):

    results = []

    for role, role_data in CAREER_ROLES.items():
        score, matched_skills = score_user_for_role(user.dict(), role_data)

        explanation = generate_explanation(
            role, score, matched_skills, role_data
        )

        results.append({
            "role": role,
            "score": score,
            **explanation
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return {
        "recommended_roles": results[:3]
    }
