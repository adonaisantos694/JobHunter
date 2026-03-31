from typing import Set, List, Dict
from models import Candidate, Job
from translations import TRANSLATIONS


def _select_top_skills(matched: Set[str], limit: int = 5) -> List[str]:
    return sorted(matched)[:limit]


def _format_list(items: List[str], fallback: str) -> str:
    return ", ".join(items) if items else fallback


def _generate_summary(matched: List[str], t: Dict) -> str:
    matched_text = _format_list(matched, t["summary_fallback"])

    return (
        f"{t['summary_base']} {matched_text}. "
        f"{t['summary_focus']} "
        f"{t['summary_extra']}"
    )


def _build_skills_section(skills: List[str], t: Dict) -> str:
    if not skills:
        return f"- {t['skills_fallback']}"

    formatted: List[str] = []

    for skill in skills:
        if skill == "python":
            formatted.append("Python (Automation, Data Processing)")
        elif skill == "sql":
            formatted.append("SQL (Data Analysis, Queries)")
        elif skill == "git":
            formatted.append("Git & Version Control")
        else:
            formatted.append(skill.capitalize())

    return "\n".join(f"- {s}" for s in formatted)


def _build_experience(t: Dict) -> str:
    blocks = []

    for title, period, items in t["experience"]:
        content = "\n".join(f"- {item}" for item in items)
        blocks.append(f"**{title}**\n{period}\n{content}")

    return "\n\n".join(blocks)


def _build_projects(t: Dict) -> str:
    projects = t["projects"]

    jobhunter = "\n".join(f"  - {item}" for item in projects["jobhunter"])
    amazon = "\n".join(f"  - {item}" for item in projects["amazon"])

    return f"""
- **JobHunter AI**
{jobhunter}

- **Amazon Sales Data Analysis**
{amazon}
"""


def generate_resume(
    candidate: Candidate,
    job: Job,
    match: float,
    lang: str = "en"
) -> str:

    t: Dict = TRANSLATIONS.get(lang, TRANSLATIONS["en"])

    matched_skills: Set[str] = candidate.skills.intersection(job.skills)
    top_skills: List[str] = _select_top_skills(matched_skills)

    summary = _generate_summary(top_skills, t)
    skills_section = _build_skills_section(top_skills, t)
    experience_section = _build_experience(t)
    projects_section = _build_projects(t)

    return f"""
{candidate.name}
{t['location']} • {candidate.phone} • {candidate.email}
GitHub: https://github.com/adonaisantos694

---

### {t['summary_title']}

{summary}

---

### {t['skills_title']}

{skills_section}

---

### {t['experience_title']}

{experience_section}

---

### {t['projects_title']}

{projects_section}

---

### {t['education_title']}

{candidate.education}

---

### {t['courses_title']}

{chr(10).join(course.capitalize() for course in candidate.courses)}
"""
