import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Define your skill keywords (you can expand this list later or use a DB)
SKILL_KEYWORDS = [
    "python", "c++", "java", "machine learning", "data analysis",
    "deep learning", "nlp", "django", "flask", "sql",
    "html", "css", "javascript", "react", "node", "linux",
    "cloud", "aws", "azure", "git", "docker"
]

def extract_skills(resume_text):
    doc = nlp(resume_text.lower())
    skills_found = []

    for token in doc:
        if token.text in SKILL_KEYWORDS:
            skills_found.append(token.text)

    return list(set(skills_found))  # Remove duplicates

# Testing it with some sample text (optional)
if __name__ == "__main__":
    sample_text = """
        I am proficient in Python, Flask, and Docker. I also have experience in AWS and Git.
    """
    print("Extracted Skills:", extract_skills(sample_text))

