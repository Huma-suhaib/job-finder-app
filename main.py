from parser import parse_resume
from job_api import find_jobs_api

# Replace with your actual resume path
resume_path = r"C:/Users/YUSUF/Desktop/Find_Jobs/resume_samples/sample_resume.pdf"  

# Extract skills
data = parse_resume(resume_path)
skills = data["skills"]
print(f"Extracted Skills: {skills}")

# Search and display jobs
for skill in skills:
    print(f"\n🔍 Jobs for skill: {skill}")
    jobs = find_jobs_api(skill)
    for i, (title, link) in enumerate(jobs, 1):
        print(f"{i}. {title} → {link}")
