from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(resume_text: str, filename: str = "resume.pdf") -> None:
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    for line in resume_text.split("\n"):
        if line.strip() == "":
            elements.append(Spacer(1, 10))
        else:
            elements.append(Paragraph(line, styles["Normal"]))

    doc.build(elements)
