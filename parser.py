from skills_extractor import extract_skills
import re
import docx2txt
import os
from pdfminer.high_level import extract_text

def extract_text_from_file(file_path):
    if file_path.endswith(".pdf"):
        return extract_text(file_path)
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format: must be PDF or DOCX")

def extract_email(text):
    match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'\b\d{10}\b', text)
    return match.group(0) if match else None

def extract_name(text):
    lines = text.strip().split('\n')
    return lines[0] if lines else "Name not found"

def parse_resume(file_path):
    text = extract_text_from_file(file_path)
    email = extract_email(text)
    phone = extract_phone(text)
    name = extract_name(text)
    skills = extract_skills(text)
    
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'skills': skills,
        'text': text
    }   

# For quick testing
if __name__ == "__main__":
    resume_path = 'resume_samples/sample_resume.pdf'
    data = parse_resume(resume_path)
    print("Parsed Resume Data:\n", data)
