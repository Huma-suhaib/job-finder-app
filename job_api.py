import requests

def find_jobs_api(skill):
    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {"query": skill, "page": "1", "num_pages": "3"}

    headers = {
        "X-RapidAPI-Key": "44c80b56fcmshaa7b755a16e639ep13b2f0jsncecee94b90ba",  #Put your real key here
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        job_links = []
        for job in data["data"][:10]:  # limit to 3 jobs per skill
            title = job.get("job_title", "No title")
            link = job.get("job_apply_link") or job.get("job_google_link", "#")
            job_links.append((title, link))
        return job_links
    else:
        print("API Error:", response.status_code)
        return []

# Test code
if __name__ == "__main__":
    skills = ["python", "flask", "aws"]
    for skill in skills:
        print(f"\nJobs for {skill}:")
        jobs = find_jobs_api(skill)
        for title, link in jobs:
            print(f"{title} → {link}")
