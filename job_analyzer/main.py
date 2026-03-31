from typing import Set, List
import sys

from models import Job, Candidate
from parser import extract_skills
from analyzer import analyze_match
from resume_generator import generate_resume
from pdf_generator import generate_pdf


def load_job_from_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def load_skills(path: str) -> Set[str]:
    with open(path, "r", encoding="utf-8") as file:
        return {line.strip().lower() for line in file if line.strip()}


def load_candidate(path: str) -> Candidate:
    name: str = ""
    email: str = ""
    birth_date: str = ""
    education: str = ""
    phone: str = ""
    courses: List[str] = []
    skills: Set[str] = set()

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    section: str = ""

    for line in lines:
        line = line.strip()

        if not line:
            continue

        lower_line = line.lower()

        if lower_line.startswith("name:"):
            name = line.split(":", 1)[1].strip()

        elif lower_line.startswith("email:"):
            email = line.split(":", 1)[1].strip()

        elif lower_line.startswith("birth_date:"):
            birth_date = line.split(":", 1)[1].strip()

        elif lower_line.startswith("education:"):
            education = line.split(":", 1)[1].strip()

        elif lower_line.startswith("phone"):
            phone = line.split(":", 1)[1].strip()

        elif lower_line.startswith("courses"):
            section = "courses"

        elif lower_line.startswith("skills"):
            section = "skills"

        elif line.endswith(":"):
            section = ""

        elif section == "courses":
            courses.append(lower_line)

        elif section == "skills":
            skills.add(lower_line)

    return Candidate(
        name=name,
        email=email,
        birth_date=birth_date,
        education=education,
        courses=courses,
        skills=skills,
        phone=phone
    )


# 🔥 NOVO: detecção simples de idioma
def detect_language(text: str) -> str:
    text = text.lower()

    pt_words = ["de", "com", "para", "em", "dados", "experiência"]
    en_words = ["the", "with", "for", "data", "experience"]

    pt_score = sum(word in text for word in pt_words)
    en_score = sum(word in text for word in en_words)

    return "pt" if pt_score > en_score else "en"


def main() -> None:
    # 🔹 Load data PRIMEIRO (pra poder detectar idioma)
    job_description: str = load_job_from_file("data/job.txt")
    known_skills: Set[str] = load_skills("data/skills.txt")
    candidate: Candidate = load_candidate("data/candidate.txt")

    # 🔹 Language: CLI OU automático
    if len(sys.argv) > 1:
        language: str = sys.argv[1].lower()
    else:
        language = detect_language(job_description)

    if language not in {"pt", "en"}:
        print("[WARN] Invalid language. Defaulting to EN.")
        language = "en"

    print(f"\n[INFO] Generating resume in: {language.upper()}")

    # 🔹 Create job
    job: Job = Job(description=job_description)

    # 🔹 Extract skills
    job.skills = extract_skills(job.description, known_skills)

    candidate.skills = extract_skills(
        " ".join(candidate.skills),
        known_skills
    )

    # 🔹 Analyze match
    match_percentage, missing_skills = analyze_match(candidate, job)

    print("\n=== MATCH RESULT ===")
    print(f"Match: {match_percentage:.2f}%")
    print(f"Missing skills: {missing_skills}")

    # 🔹 Generate resume
    resume: str = generate_resume(candidate, job, match_percentage, language)

    # 🔹 Generate PDF
    output_file = f"output_resume_{language}.pdf"
    generate_pdf(resume, output_file)

    print(f"\n[INFO] PDF successfully generated: {output_file}")


if __name__ == "__main__":
    main()
