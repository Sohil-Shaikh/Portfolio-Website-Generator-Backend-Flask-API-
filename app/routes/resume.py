# app/routes/resume.py
from flask import Blueprint, request, jsonify
import pdfplumber
from docx import Document
import re

resume_api = Blueprint('resume_api', __name__)

def parse_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def parse_doc(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])



def extract_details(text):
    # Normalize text
    text = text.strip()

    # Extract name (first line)
    name = text.split('\n')[0].strip()

    # Extract email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    email = email_match.group(0) if email_match else None

    # Extract phone number
    phone_match = re.search(r'\+?\d[\d\s]{9,}', text)
    phone = phone_match.group(0).strip() if phone_match else None

    # Extract education (simplified)
    education = []
    if "Education" in text:
        edu_block = text.split("Education")[1][:300]
        for line in edu_block.split('\n'):
            if "B.E." in line or "B.Tech" in line or "Bachelor" in line:
                education.append({"degree": line.strip(), "institute": "Sant Gadge Baba"})

    # Extract skills (basic keyword match)
    skills_keywords = ["Python", "Flask", "React", "HTML", "CSS", "JavaScript", "SQL", "Django"]
    skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]

    # Extract experience (mock until we implement more logic)
    experience = []
    if "Intern" in text or "Project" in text:
        experience.append({"company": "Some Project/Internship", "role": "Intern/Contributor"})

    return {
        "hero": {
            "name": name,
            "tagline": "Aspiring Developer"
        },
        "about": {
            "bio": text[:300]  # First 300 characters as bio
        },
        "skills": skills,
        "experience": experience,
        "education": education,
        "contact": {
            "email": email,
            "phone": phone
        }
    }



@resume_api.route('/upload_resume', methods=['POST'])
def upload_resume():
    file = request.files.get('resume')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    text = parse_pdf(file) if file.filename.endswith('.pdf') else parse_doc(file)
    data = extract_details(text)
    
    print("Parsed text:\n", text[:500])  # Show sample
    print("Structured data:\n", data)

    return jsonify(data)

