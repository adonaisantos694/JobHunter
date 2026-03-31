# 🚀 JobHunter AI

**JobHunter AI** is an intelligent Python application designed to automate and optimize the job application process.

It analyzes job descriptions, evaluates candidate profiles, and generates **customized, job-specific resumes in PDF format** — eliminating the need to manually rewrite CVs for every application.

> Built to simulate how recruiters evaluate candidates — but faster, consistent, and scalable.

---

## 🎯 Key Features

### 🤖 Intelligent Resume Generation
- Automatically creates tailored resumes based on job descriptions
- Highlights the most relevant skills for each position

### 📊 Skill Matching Engine
- Compares candidate skills vs job requirements
- Calculates a **match percentage**
- Identifies missing skills

### 🌍 Multilingual Support
- Supports **English and Portuguese**
- Generates resumes in the selected language

### ⚡ Efficiency & Automation
- Eliminates repetitive resume editing
- Speeds up job application workflows
- Clean, modular architecture

### 📄 PDF Export
- Generates professional resumes using `reportlab`
- Ready-to-send output for recruiters

---

## 🧠 How It Works

The system follows a structured pipeline:

1. **Read Job Description**
   - Loads data from `data/job.txt`

2. **Parse Candidate Profile**
   - Extracts relevant information from `data/candidate.txt`

3. **Skill Extraction**
   - Uses `skills.txt` to identify relevant keywords

4. **Match Analysis**
   - Compares candidate vs job skills
   - Calculates match percentage
   - Detects missing skills

5. **Resume Generation**
   - Builds a dynamic, tailored CV
   - Adapts content based on job requirements

6. **PDF Export**
   - Generates a professional PDF resume

---

## 🧱 Project Structure

job_analyzer/

├── main.py # Entry point (orchestrates the flow)
├── models.py # Data structures (Candidate, Job)
├── parser.py # Text parsing and skill extraction
├── analyzer.py # Matching logic and scoring
├── resume_generator.py # Dynamic resume builder (EN/PT)
├── pdf_generator.py # PDF export (reportlab)
├── translations.py # Multilingual support

├── data/
│ ├── job.txt
│ ├── candidate.txt
│ └── skills.txt


---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/jobhunter-ai.git
cd jobhunter-ai

pip install -r requirements.txt

▶️ Usage

To run the project correctly, you must navigate to the job_analyzer directory first.

1. Go to the project folder
cd jobhunter-ai
2. Navigate to the application directory
cd job_analyzer
3. Run the application

Choose the language for the generated resume:

🇧🇷 Portuguese Resume
python main.py pt
🇺🇸 English Resume
python main.py en
🧠 Command Explanation
cd jobhunter-ai
Moves into the main project folder
cd job_analyzer
Enters the application directory where the code actually runs
python main.py pt
Runs the program and generates the resume in Portuguese
python main.py en
Runs the program and generates the resume in English
📁 Input Files

Ensure the following files are properly filled:

data/job.txt → Job description
data/candidate.txt → Candidate profile
data/skills.txt → List of recognized skills
📈 Example Output
Match Percentage: 81.82%
Missing Skills: ['X', 'Y']
Generated File: custom_resume.pdf
🧩 Tech Stack
Python
ReportLab (PDF generation)
Modular architecture
💡 Future Improvements
NLP-based skill extraction (spaCy / transformers)
Web interface (Streamlit or FastAPI)
Integration with job platforms (LinkedIn, etc.)
AI-powered resume optimization suggestions
📌 Why This Project Matters

Recruiters spend seconds scanning resumes.
Candidates spend hours rewriting them.

JobHunter AI eliminates that inefficiency.

👨‍💻 Author

Developed by Adonai dos Santos Soares

📄 License

This project is open-source and available under the MIT License.


