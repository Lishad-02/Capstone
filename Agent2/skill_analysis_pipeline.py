import pandas as pd
import json
import os
from collections import Counter
import google.generativeai as genai


GEMINI_API_KEY = ""  
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ==== STEP 1: SKILL FREQUENCY EXTRACTION ====
def extract_skills_frequency(csv_file):
    df = pd.read_csv(csv_file)
    skill_columns = [col for col in df.columns if col.lower().startswith('skill')]
    all_skills = []
    for col in skill_columns:
        all_skills += df[col].dropna().astype(str).str.strip().str.lower().tolist()
    skill_freq = dict(Counter(all_skills))
    sorted_freq = dict(sorted(skill_freq.items(), key=lambda x: x[1], reverse=True))
    return sorted_freq

# ==== STEP 2: CLASSI PROMPT ====
def build_classify_prompt(skill_freq: dict):
    return f"""
You are a senior software engineering recruiter.

Below is a dictionary of skills with their frequency from real job circulars:

{json.dumps(skill_freq, indent=2)}

Your task is to analyze this list and categorize the most relevant skills into three groups:

1. **Must Needed** (exactly 5-10): 
   - Core, foundational skills needed in most software engineering jobs today.
   - High frequency and high importance.
   

2. **Moderately Needed** (5 to 7): 
   - Commonly expected or beneficial, but not strictly required everywhere.
   
3. **Extra Skills** (3 to 5): 
   - Niche, specialized, or lower-priority skills that can still add value.
   

 Your categorization must balance **frequency** and **industry importance**, not just popularity.

 Output format (no explanation, no extra text):
Must Needed: [...]
Moderately Needed: [...]
Extra Skills: [...]
"""

# ==== STEP 3: CLASSIFY SKILLS ====
def classify_skills(skill_freq: dict):
    prompt = build_classify_prompt(skill_freq)
    response = model.generate_content(prompt)
    return response.text.strip()

# ==== STEP 4: REPLACEMENT PROMPT ====
def build_comparison_prompt(global_result, bd_result):
    return f"""
You are a senior software engineering hiring expert.

Below are two categorized skill sets extracted from global and Bangladesh-based software engineering job datasets.

--- Global ---
{global_result}

--- Bangladesh ---
{bd_result}

 Your goal is to identify functionally **equivalent but different** skills used in Bangladesh that can replace global skills.

 Follow these strict rules:

1. Focus **only** on Global “Must Needed” skills.
2. For each Global Must skill:
   - If it is **NOT present** in Bangladesh “Must Needed”, check if a functionally **equivalent skill** exists in BD’s “Moderately Needed” or “Extra Skills”.
   - Only suggest a replacement if it performs the **same technical role** or is used in the **same context** in real software jobs. For example:
     - MongoDB (Global) → SQL (BD): both are databases
     - Python (Global) → Java (BD): both are backend languages
     - React (Global) → Vue or Angular (BD): both are frontend frameworks
     - Docker (Global) → Spring Boot or Cloud (BD): both help in deployment
     - AWS (Global) → Cloud (BD): general cloud platform
3.  DO NOT suggest:
   - The same skill (e.g., AWS → AWS)
   - Minor spelling or word form differences (e.g., API → APIs, RESTful → REST)
   - Skills already in BD “Must Needed”

4.  Only suggest **real replacements** where a different tool/tech is used for the same purpose.

 Output format only:
Replacement Suggestions:
- BD_Skill (instead of Global_Skill)
- ...
(no explanation, no justification)
"""

# ==== STEP 5: COMPARE ====
def compare_global_bd(global_result, bd_result):
    prompt = build_comparison_prompt(global_result, bd_result)
    response = model.generate_content(prompt)
    return response.text.strip()

# ==== MAIN ====
def run_full_pipeline():
    global_freq = extract_skills_frequency("data/global_jobs.csv")
    bd_freq = extract_skills_frequency("data/bd_jobs.csv")

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/global_skill_freq.json", "w") as f:
        json.dump(global_freq, f, indent=2)
    with open("outputs/bd_skill_freq.json", "w") as f:
        json.dump(bd_freq, f, indent=2)

    global_result = classify_skills(global_freq)
    bd_result = classify_skills(bd_freq)

    with open("outputs/global_classified.txt", "w", encoding="utf-8") as f:
        f.write(global_result)
    with open("outputs/bd_classified.txt", "w", encoding="utf-8") as f:
        f.write(bd_result)

    comparison_result = compare_global_bd(global_result, bd_result)
    with open("outputs/replacement_suggestions.txt", "w", encoding="utf-8") as f:
        f.write(comparison_result)

    print("\n📌 Global Recommendations:\n")
    print(global_result)
    print("\n📌 Bangladesh Recommendations:\n")
    print(bd_result)
    print("\n Specialized BD Replacements:\n")
    print(comparison_result)

# ==== RUN ====
if __name__ == "__main__":
    run_full_pipeline()
