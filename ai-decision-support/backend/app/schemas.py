from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    skills: List[str]
    interests: List[str]
    strengths: List[str]
