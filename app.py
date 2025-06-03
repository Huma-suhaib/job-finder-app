from flask import Flask, render_template, request
from parser import parse_resume
from job_api import find_jobs_api
import os

app = Flask(__name__)

# Homepage route: loads with no jobs
@app.route("/", methods=["GET", "POST"])
def home():
    job_urls = []
    
    if request.method == "POST":
        # 1) Check for the file
        if "resume" not in request.files:
            return "No file part", 400
        
        resume_file = request.files["resume"]
        if resume_file.filename == "":
            return "No selected file", 400
        
        # 2) Save it to a temporary location
        save_dir = os.path.join(os.getcwd(), "uploads")
        os.makedirs(save_dir, exist_ok=True)
        resume_path = os.path.join(save_dir, resume_file.filename)
        resume_file.save(resume_path)

        # 3) Parse and extract skills
        data = parse_resume(resume_path)
        skills = data.get("skills", [])

        # 4) For each skill, fetch job URLs
        for skill in skills:
            # find_jobs_api should return a list of (title, link) tuples
            jobs_for_this_skill = find_jobs_api(skill)
            # We’ll collect only the URL itself (or you can store (title,link))
            for (_title, link) in jobs_for_this_skill:
                job_urls.append(link)

    # Render template with job URLs
    return render_template("index.html", jobs=job_urls)

if __name__ == "__main__":
    app.run(debug=True)
