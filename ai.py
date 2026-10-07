import streamlit as st
from groq import Groq


MODEL = "openai/gpt-oss-120b"


def get_client():

    return Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )


def ask_ai(question, profile=None):

    client = get_client()

    profile_text = ""

    if profile:

        profile_text = f"""
Student profile:

Name: {profile.get("name", "Not provided")}
Intermediate group: {profile.get("education", "Not provided")}
Percentage: {profile.get("percentage", "Not provided")}
Location: {profile.get("location", "Not provided")}
Budget: {profile.get("budget", "Not provided")}
Interests: {", ".join(profile.get("interests", []))}
Career goal: {profile.get("career_goal", "Not decided")}
"""

    system_prompt = """
You are EduPath AI, a friendly education and career guidance
assistant for students in Pakistan who have completed Intermediate,
FSc, ICS, I.Com or FA.

Use simple language.

Help students understand:
- degrees
- universities
- careers
- scholarships
- entrance tests
- admissions
- skills

Do not present uncertain information as confirmed fact.

If discussing admission requirements, fees or deadlines,
tell the student to verify the information on the official
university or scholarship website.

Never guarantee admission or scholarships.

Do not make decisions for the student.
Help them make informed decisions.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": profile_text + "\n\nQuestion:\n" + question,
            },
        ],
        temperature=0.4,
        max_tokens=2000,
    )

    return response.choices[0].message.content


def get_recommendations(profile):

    question = """
Based on this student's profile, create personalized recommendations.

Give:

1. Top 3 suitable degree programs
2. Why each degree fits
3. Potential career paths
4. Skills the student should start learning
5. What type of universities they should consider
6. Their recommended next 3 actions

Keep the answer practical and beginner-friendly.

Do not invent exact admission requirements or deadlines.
"""

    return ask_ai(
        question,
        profile=profile,
    )
