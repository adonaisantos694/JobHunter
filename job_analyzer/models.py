from dataclasses import dataclass, field
from typing import List, Set


@dataclass
class Job:
    description: str
    skills: Set[str] = field(default_factory=set)


@dataclass
class Candidate:
    name: str
    email: str
    birth_date: str
    education: str
    courses: List[str]
    skills: Set[str]
    phone: str = ""
