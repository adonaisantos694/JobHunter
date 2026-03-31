from typing import Dict, List


TRANSLATIONS: Dict[str, Dict[str, object]] = {
    "en": {
        "location": "Brazil",

        "summary_title": "PROFESSIONAL SUMMARY",
        "skills_title": "TECHNICAL SKILLS",
        "experience_title": "PROJECT EXPERIENCE",
        "projects_title": "KEY PROJECTS",
        "education_title": "EDUCATION",
        "courses_title": "COURSES",

        "summary_base": "Junior Python Developer with hands-on experience in",
        "summary_fallback": "relevant technologies",
        "summary_focus": "Focused on automation, data processing, and building real-world solutions.",
        "summary_extra": "Strong emphasis on clean code, efficiency, and solving practical problems.",

        "skills_fallback": "Adaptable to various technologies",

        "experience": [
            ("Python Developer – Independent Projects", "2024 – 2025", [
                "Developed automation scripts to eliminate repetitive manual tasks",
                "Built data processing workflows using Python and SQL",
                "Applied clean code practices to ensure readability and maintainability",
            ]),
            ("Junior Programmer (Self-Directed Practice)", "2023 – 2024", [
                "Created Python projects focused on automation and problem solving",
                "Strengthened programming logic and debugging skills",
            ]),
            ("Programming Student", "2022 – 2023", [
                "Learned core programming concepts and built foundational projects",
            ]),
        ],

        "projects": {
            "jobhunter": [
                "Built a system to analyze job descriptions and generate tailored resumes",
                "Reduced application time from 20 minutes to 2 minutes",
                "Implemented skill matching and dynamic resume generation",
            ],
            "amazon": [
                "Developed automated data pipelines using Python and SQL",
                "Transformed raw data into actionable insights",
                "Improved decision-making through structured analysis",
            ],
        }
    },

    "pt": {
        "location": "Brasil",

        "summary_title": "RESUMO PROFISSIONAL",
        "skills_title": "HABILIDADES TÉCNICAS",
        "experience_title": "EXPERIÊNCIA EM PROJETOS",
        "projects_title": "PRINCIPAIS PROJETOS",
        "education_title": "EDUCAÇÃO",
        "courses_title": "CURSOS",

        "summary_base": "Desenvolvedor Python Júnior com experiência prática em",
        "summary_fallback": "tecnologias relevantes",
        "summary_focus": "Focado em automação, processamento de dados e criação de soluções reais.",
        "summary_extra": "Forte ênfase em código limpo, eficiência e resolução de problemas práticos.",

        "skills_fallback": "Adaptável a diversas tecnologias",

        "experience": [
            ("Desenvolvedor Python – Projetos Independentes", "2024 – 2025", [
                "Desenvolveu scripts de automação para eliminar tarefas manuais repetitivas",
                "Criou fluxos de processamento de dados com Python e SQL",
                "Aplicou boas práticas de código limpo para garantir legibilidade e manutenção",
            ]),
            ("Programador Júnior (Prática Autodidata)", "2023 – 2024", [
                "Desenvolveu projetos em Python focados em automação e resolução de problemas",
                "Aprimorou lógica de programação e debugging",
            ]),
            ("Estudante de Programação", "2022 – 2023", [
                "Aprendeu fundamentos de programação e desenvolveu projetos iniciais",
            ]),
        ],

        "projects": {
            "jobhunter": [
                "Desenvolveu um sistema para analisar vagas e gerar currículos personalizados",
                "Reduziu o tempo de candidatura de 20 minutos para 2 minutos",
                "Implementou matching de habilidades e geração dinâmica de currículo",
            ],
            "amazon": [
                "Desenvolveu pipelines automatizados de análise de dados com Python e SQL",
                "Transformou dados brutos em insights acionáveis",
                "Apoiou a tomada de decisão com análises estruturadas",
            ],
        }
    }
}
