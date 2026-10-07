import streamlit as st

from ai import ask_ai, get_recommendations
from agent import (
    compare_universities,
    create_application_checklist,
    find_matching_scholarships,
)
from data import (
    get_universities,
    get_degrees,
    get_scholarships,
    get_entrance_tests,
)
from style import apply_styles


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="EduPath AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_styles()


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "profile" not in st.session_state:
    st.session_state.profile = {}

if "saved" not in st.session_state:
    st.session_state.saved = []

if "deadlines" not in st.session_state:
    st.session_state.deadlines = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "agent_result" not in st.session_state:
    st.session_state.agent_result = None


# ---------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"


def navigate(page):
    st.session_state.page = page


# ---------------------------------------------------------
# TOP NAVIGATION
# ---------------------------------------------------------

st.markdown(
    """
    <div class="topbar">
        <div class="brand">
            <div class="brand-icon">🎓</div>
            <div>
                <div class="brand-name">EduPath AI</div>
                <div class="brand-tagline">Your next step after Intermediate</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

nav_cols = st.columns(7)

nav_items = [
    ("Home", "Home"),
    ("Profile", "Profile"),
    ("Advisor", "AI Advisor"),
    ("Chat", "AI Chat"),
    ("Agent", "AI Agent"),
    ("Explore", "Explore"),
    ("Saved", "Saved"),
]

for col, (label, page) in zip(nav_cols, nav_items):
    with col:
        if st.button(label, use_container_width=True):
            navigate(page)


st.markdown("<div class='nav-line'></div>", unsafe_allow_html=True)


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.markdown(
        """
        <section class="hero">
            <div class="hero-badge">✨ AI-powered guidance for Pakistani students</div>

            <h1>
                You passed Intermediate.<br>
                <span>What comes next?</span>
            </h1>

            <p>
                Discover the right degree, university, scholarship and career
                path based on your marks, interests, location and goals.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns([1, 1])

    with c1:
        if st.button(
            "🚀 Build My Roadmap",
            use_container_width=True,
            type="primary",
        ):
            navigate("Profile")

    with c2:
        if st.button(
            "🤖 Ask EduPath AI",
            use_container_width=True,
        ):
            navigate("AI Chat")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-title">
            <span>Everything you need for your next step</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cards = [
        (
            "🎯",
            "Personalized Guidance",
            "Get degree and career recommendations based on your profile.",
        ),
        (
            "🏫",
            "University Discovery",
            "Explore Pakistani universities and programs that fit you.",
        ),
        (
            "💰",
            "Scholarship Finder",
            "Discover scholarship and financial-aid opportunities.",
        ),
        (
            "🧠",
            "AI Agent",
            "Let an AI agent compare options and create your application plan.",
        ),
    ]

    cols = st.columns(4)

    for col, (icon, title, description) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="info-banner">
            <strong>🤖 AI Transparency</strong>
            <br>
            EduPath AI provides AI-generated guidance. Always verify
            admission requirements, fees and deadlines on the official
            university or scholarship website before applying.
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.markdown(
        """
        <div class="page-heading">
            <div class="eyebrow">YOUR PROFILE</div>
            <h1>Tell us about yourself</h1>
            <p>
                The more we know about your academic goals, the more useful
                your recommendations become.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    profile = st.session_state.profile

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Your name",
            value=profile.get("name", ""),
            placeholder="e.g. Ali Ahmed",
        )

        education = st.selectbox(
            "Intermediate group",
            [
                "FSc Pre-Engineering",
                "FSc Pre-Medical",
                "ICS",
                "I.Com",
                "FA / Humanities",
                "Other",
            ],
            index=0,
        )

        percentage = st.number_input(
            "Intermediate percentage",
            min_value=0.0,
            max_value=100.0,
            value=float(profile.get("percentage", 70)),
        )

        location = st.selectbox(
            "Preferred study location",
            [
                "Karachi",
                "Lahore",
                "Islamabad / Rawalpindi",
                "Peshawar",
                "Quetta",
                "Anywhere in Pakistan",
                "Abroad",
            ],
        )

    with col2:

        budget = st.selectbox(
            "Study budget",
            [
                "Scholarship / Financial Aid Required",
                "Low Cost",
                "Under PKR 100,000 per year",
                "PKR 100,000–300,000 per year",
                "PKR 300,000–600,000 per year",
                "Above PKR 600,000 per year",
            ],
        )

        interests = st.multiselect(
            "Your interests",
            [
                "Artificial Intelligence",
                "Software Development",
                "Data Science",
                "Cybersecurity",
                "Engineering",
                "Medicine",
                "Business",
                "Finance",
                "Design",
                "Education",
                "Research",
            ],
        )

        career_goal = st.text_input(
            "Career goal",
            value=profile.get("career_goal", ""),
            placeholder="e.g. AI Engineer",
        )

    if st.button(
        "💾 Save My Profile",
        use_container_width=True,
        type="primary",
    ):

        st.session_state.profile = {
            "name": name,
            "education": education,
            "percentage": percentage,
            "location": location,
            "budget": budget,
            "interests": interests,
            "career_goal": career_goal,
        }

        st.success("Your profile has been saved!")

        st.session_state.page = "AI Advisor"
        st.rerun()


# =========================================================
# AI ADVISOR
# =========================================================

elif st.session_state.page == "AI Advisor":

    st.markdown(
        """
        <div class="page-heading">
            <div class="eyebrow">AI ADVISOR</div>
            <h1>Your personalized recommendations</h1>
            <p>
                Based on your academic profile, interests and goals.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.profile:

        st.markdown(
            """
            <div class="empty-state">
                <div class="empty-icon">👤</div>
                <h2>Complete your profile first</h2>
                <p>
                    Tell us about your Intermediate subjects, interests,
                    budget and career goals.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Create My Profile", type="primary"):
            navigate("Profile")

    else:

        profile = st.session_state.profile

        st.markdown(
            f"""
            <div class="profile-summary">
                <strong>{profile.get("name", "Student")}</strong>
                <span>{profile.get("education", "")}</span>
                <span>{profile.get("percentage", 0)}%</span>
                <span>{profile.get("location", "")}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "✨ Generate My Recommendations",
            use_container_width=True,
            type="primary",
        ):

            with st.spinner("Analyzing your profile..."):
                result = get_recommendations(profile)

            st.markdown(
                f"""
                <div class="ai-result">
                    {result}
                </div>
                """,
                unsafe_allow_html=True,
            )


# =========================================================
# AI CHAT
# =========================================================

elif st.session_state.page == "AI Chat":

    st.markdown(
        """
        <div class="page-heading">
            <div class="eyebrow">EDUPATH AI</div>
            <h1>Ask anything about your next step</h1>
            <p>
                Ask about degrees, careers, universities, admissions,
                scholarships or entrance tests.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for message in st.session_state.chat_history:

        if message["role"] == "user":
            st.markdown(
                f"""
                <div class="chat-user">
                    {message["content"]}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="chat-ai">
                    <strong>🤖 EduPath AI</strong>
                    <br><br>
                    {message["content"]}
                </div>
                """,
                unsafe_allow_html=True,
            )

    question = st.chat_input(
        "Ask EduPath AI..."
    )

    if question:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.spinner("Thinking..."):

            response = ask_ai(
                question,
                profile=st.session_state.profile,
            )

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        st.rerun()


# =========================================================
# AGENT
# =========================================================

elif st.session_state.page == "AI Agent":

    st.markdown(
        """
        <div class="page-heading">
            <div class="eyebrow">AGENTIC AI</div>
            <h1>Let EduPath work through the problem</h1>
            <p>
                The agent can research, compare and prepare plans for you.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.profile:

        st.warning("Please complete your profile first.")

    else:

        task = st.selectbox(
            "What would you like the agent to do?",
            [
                "Compare universities for me",
                "Find scholarships for me",
                "Create my application checklist",
            ],
        )

        if st.button(
            "🧠 Run Agent",
            use_container_width=True,
            type="primary",
        ):

            with st.spinner("Agent is working..."):

                if task == "Compare universities for me":

                    result = compare_universities(
                        st.session_state.profile
                    )

                elif task == "Find scholarships for me":

                    result = find_matching_scholarships(
                        st.session_state.profile
                    )

                else:

                    result = create_application_checklist(
                        st.session_state.profile
                    )

                st.session_state.agent_result = result

        if st.session_state.agent_result:

            st.markdown(
                """
                <div class="agent-label">
                    🧠 AGENT RESULT
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                st.session_state.agent_result
            )

            st.markdown(
                """
                <div class="confirmation-box">
                    <strong>Before you take action</strong><br>
                    Review the recommendations carefully.
                    EduPath AI does not automatically submit applications
                    or make consequential decisions for you.
                </div>
                """,
                unsafe_allow_html=True,
            )

            c1, c2 = st.columns(2)

            with c1:
                if st.button(
                    "❤️ Save Result",
                    use_container_width=True,
                ):
                    st.session_state.saved.append(
                        st.session_state.agent_result
                    )
                    st.success("Saved!")

            with c2:
                if st.button(
                    "Clear",
                    use_container_width=True,
                ):
                    st.session_state.agent_result = None
                    st.rerun()


# =========================================================
# EXPLORE
# =========================================================

elif st.session_state.page == "Explore":

    st.markdown(
        """
        <div class="page-heading">
            <div class="eyebrow">EXPLORE</div>
            <h1>Discover your opportunities</h1>
            <p>
                Explore sample Pakistani education opportunities.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    category = st.selectbox(
        "Explore",
        [
            "Universities",
            "Degrees",
            "Scholarships",
            "Entrance Tests",
        ],
    )

    if category == "Universities":

        universities = get_universities()

        for university in universities:

            st.markdown(
                f"""
                <div class="listing-card">
                    <div>
                        <h3>🏫 {university["name"]}</h3>
                        <p>
                            {university["city"]} · {university["type"]}
                        </p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    elif category == "Degrees":

        for degree in get_degrees():

            st.markdown(
                f"""
                <div class="listing-card">
                    <h3>🎓 {degree["name"]}</h3>
                    <p>{degree["description"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    elif category == "Scholarships":

        for scholarship in get_scholarships():

            st.markdown(
                f"""
                <div class="listing-card">
                    <h3>💰 {scholarship["name"]}</h3>
                    <p>{scholarship["description"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    else:

        for test in get_entrance_tests():

            st.markdown(
                f"""
                <div class="listing-card">
                    <h3>📝 {test["name"]}</h3>
                    <p>{test["description"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


# =========================================================
# SAVED
# =========================================================

elif st.session_state.page == "Saved":

    st.markdown(
        """
        <div class="page-heading">
            <div class="eyebrow">MY SPACE</div>
            <h1>Saved opportunities</h1>
            <p>
                Keep useful recommendations in one place.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.saved:

        st.markdown(
            """
            <div class="empty-state">
                <div class="empty-icon">🔖</div>
                <h2>Nothing saved yet</h2>
                <p>
                    Your saved universities, scholarships and plans
                    will appear here.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        for item in st.session_state.saved:

            st.markdown(
                f"""
                <div class="listing-card">
                    {item}
                </div>
                """,
                unsafe_allow_html=True,
            )
