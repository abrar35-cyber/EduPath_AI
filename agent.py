from ai import ask_ai
from data import (
    get_universities,
    get_scholarships,
)


def compare_universities(profile):

    universities = get_universities()

    location = profile.get(
        "location",
        "Anywhere in Pakistan",
    )

    relevant = universities

    if location not in [
        "Anywhere in Pakistan",
        "Abroad",
    ]:

        relevant = [
            university
            for university in universities
            if university["city"] == location
        ]

    university_text = "\n".join(
        [
            f"""
University: {u["name"]}
City: {u["city"]}
Type: {u["type"]}
Programs: {", ".join(u["programs"])}
"""
            for u in relevant
        ]
    )

    prompt = f"""
You are the EduPath AI university comparison agent.

Student profile:
{profile}

Available university data:
{university_text}

Compare the most relevant universities for this student.

Include:
- university
- why it may fit
- relevant programs
- strengths
- things the student should verify
- recommended next step

Do not invent missing facts.
"""

    return ask_ai(prompt, profile)


def find_matching_scholarships(profile):

    scholarships = get_scholarships()

    scholarship_text = "\n".join(
        [
            f"""
Name: {s["name"]}
Type: {s["type"]}
Description: {s["description"]}
"""
            for s in scholarships
        ]
    )

    prompt = f"""
You are the EduPath scholarship agent.

Student profile:
{profile}

Available scholarships:
{scholarship_text}

Identify the most relevant opportunities.

Explain:
- why it may be relevant
- what the student should verify
- what documents may commonly be needed
- what the next action should be

Never claim that the student is definitely eligible.
"""

    return ask_ai(prompt, profile)


def create_application_checklist(profile):

    prompt = f"""
You are the EduPath application planning agent.

Student profile:
{profile}

Create a general university application checklist
for a Pakistani Intermediate student.

Include:

1. Academic documents
2. Identity documents
3. Entry test preparation
4. University research
5. Financial aid research
6. Application submission
7. Final verification

Clearly mark steps that depend on the specific university.

Do not invent university-specific requirements.
"""

    return ask_ai(prompt, profile)
