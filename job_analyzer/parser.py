from typing import Set


def extract_skills(text: str, known_skills: Set[str]) -> Set[str]:
    normalized_text: str = text.lower()
    found_skills: Set[str] = set()

    for skill in known_skills:
        if skill in normalized_text:
            found_skills.add(skill)

    return found_skills
