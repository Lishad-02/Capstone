# **AI Agent for Career Path & Subject Recommendation Based on User Traits and Localized Data (Bangladesh) **



## Subject Recommendation System
Based on a student's preferences, strengths, study habits, and mental effort capacity, suggest best-fit academic subjects or fields of study
 

*Sample Student Input*:

Problem solver 
Hates reading-heavy material 
Prefers lab & hands-on
Target CGPA: 3.8
Can study 3 hrs/day
Presentation: not confident/less

**Sample Our Agent's Outnput**:

Best-fit subjects: Computer Science , Data Science
Avoid: Law, Literature, Philosophy
Study plan: For CGPA 3.8, focus 40% time on programming, 30% on applied math
Soft skill booster: Improve Speaking capabilities

**Sample dataset:**
subject recommender: Learning preferences, Avg Study Time, Extra project cost ,CGPA , For get high CGPA need to improve?, Job opportunity, Research Scope, Introvert/Extrovert,Public Speaking Skill,Group Work or Individual work, Satisfaction Level, Exam Pressure, Memory Retention,problem-solving strengths, Theory vs. practical .

samples : minimum 500 
additional 500 via GPT synthetic generation if not possible to collect






## Career Path Guidance 

**Sample Dataset:**

Scrapes:

BDjobs
chakri.com
O*NET
Glassdoor
Levels.fyi
LinkedIn Salary Insights

Features:
job_title ,	required_skills	workload , avg_salary ,	mental_satisfaction , education , growth_path , soft_skills , Language

Survey Data:

Actual workload & mental pressure,
Growth chances,
Real required skills ,
Job satisfaction and lifestyle

mail,interview,reddit,fb group etc




## for NLP + Input Understanding

5,000–10,000 sentences with:

Free-form user preferences ("I hate reading", "Love teamwork", etc.)

Aspect + Sentiment pair (e.g., {"reading": negative})

sources:

Reddit (r/college, r/careerguidance)
Quora, Twitter
GPT-assisted: Generate sentences for common traits

OR

 fine-tune bert-base-uncased for sentiment + aspect extraction


## Tech Needed

Suggestion/Prediction: 
ML-DL Model: XGBoost,Random Forest,Feedforward Neural Network 

NLP: Job Title Understanding ---->BERT / Sentence-BERT (SBERT)

extra:
BERT classifier to train on it if doing custom sentiment scoring.