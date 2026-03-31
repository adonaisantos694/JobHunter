from typing import Set, Tuple
from models import Candidate, Job


def analyze_match(candidate: Candidate, job: Job) -> Tuple[float, Set[str]]:
    if not job.skills:
        return 0.0, set()

    matched_skills: Set[str] = candidate.skills & job.skills
    missing_skills: Set[str] = job.skills - candidate.skills

    match_percentage: float = (len(matched_skills) / len(job.skills)) * 100

    return match_percentage, missing_skills
