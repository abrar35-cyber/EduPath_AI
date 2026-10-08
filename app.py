import streamlit as st
from textwrap import dedent

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


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="EduPath AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_styles()


# =========================================================
# SESSION STATE
# =========================================================

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

if "page" not in st.session_state:
    st.session_state.page = "Home"


def navigate(page):
    st.session_state.page = page


# =========================================================
# TOP BAR
# =========================================================

st.markdown(
    dedent(
        """
        <div class="topbar">
            <div class="brand">
                <div class="brand-icon">🎓</div>
                <div>
                    <div class="brand-name">EduPath AI</div>
                    <div class="brand-tagline">
                        Your next step after Intermediate
                    </div>
                </div>
            </div>
        </div>
        """
    ),
    unsafe_allow_html=True,
)


# =========================================================
# NAVIGATION
# =========================================================

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
        if st.button(
            label,
            key=f"nav_{page}",
            use_container_width=True,
        ):
            navigate(page)
            st.rerun()


st.markdown(
    "<div class='nav-line'></div>",
    unsafe_allow_html=True,
)


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    # -------------------------
    # HERO
    # -------------------------

    st.markdown(
        dedent(
            """
            <section class="hero">

                <div class="hero-badge">
                    ✨ AI-powered guidance for Pakistani students
                </div>

                <h1>
                    You passed Intermediate.<br>
                    <span>What comes next?</span>
                </h1>

                <p>
                    Discover the right degree, university, scholarship
                    and career path based on your marks, interests,
                    location and goals.
                </p>

            </section>
            """
        ),
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "🚀 Build My Roadmap",
            key="home_roadmap",
            use_container_width=True,
            type="primary",
        ):
            navigate("Profile")
            st.rerun()

    with c2:
        if st.button(
            "🤖 Ask EduPath AI",
            key="home_chat",
            use_container_width=True,
        ):
            navigate("AI Chat")
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------
    # SECTION TITLE
    # -------------------------

    st.markdown(
        dedent(
            """
            <div class="section-title">
                Everything you need for your next step
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    # -------------------------
    # FEATURE CARDS
    # -------------------------

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
                dedent(
                    f"""
                    <div class="feature-card">
                        <div class="feature-icon">{icon}</div>
                        <h3>{title}</h3>
                        <p>{description}</p>
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------
    # AI TRANSPARENCY
    # -------------------------

    st.markdown(
        dedent(
            """
            <div class="info-banner">
                <strong>🤖 AI Transparency</strong>
                <br>
                EduPath AI provides AI-generated guidance.
                Always verify admission requirements, fees and
                deadlines on the official university or scholarship
                website before applying.
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.markdown(
        dedent(
            """
            <div class="page-heading">
                <div class="eyebrow">YOUR PROFILE</div>
                <h1>Tell us about yourself</h1>
                <p>
                    The more we know about your academic goals,
                    the more useful your recommendations become.
                </p>
            </div>
            """
        ),
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

        education_options = [
            "FSc Pre-Engineering",
            "FSc Pre-Medical",
            "ICS",
            "I.Com",
            "FA / Humanities",
            "Other",
        ]

        current_education = profile.get(
            "education",
            education_options[0],
        )

        education_index = (
            education_options.index(current_education)
            if current_education in education_options
            else 0
        )

        education = st.selectbox(
            "Intermediate group",
            education_options,
            index=education_index,
        )

        percentage = st.number_input(
            "Intermediate percentage",
            min_value=0.0,
            max_value=100.0,
            value=float(profile.get("percentage", 70)),
        )

        location_options = [
            "Karachi",
            "Lahore",
            "Islamabad / Rawalpindi",
            "Peshawar",
            "Quetta",
            "Anywhere in Pakistan",
            "Abroad",
        ]

        current_location = profile.get(
            "location",
            location_options[0],
        )

        location_index = (
            location_options.index(current_location)
            if current_location in location_options
            else 0
        )

        location = st.selectbox(
            "Preferred study location",
            location_options,
            index=location_index,
        )

    with col2:

        budget_options = [
            "Scholarship / Financial Aid Required",
            "Low Cost",
            "Under PKR 100,000 per year",
            "PKR 100,000–300,000 per year",
            "PKR 300,000–600,000 per year",
            "Above PKR 600,000 per year",
        ]

        current_budget = profile.get(
            "budget",
            budget_options[0],
        )

        budget_index = (
            budget_options.index(current_budget)
            if current_budget in budget_options
            else 0
        )

        budget = st.selectbox(
            "Study budget",
            budget_options,
            index=budget_index,
        )

        interest_options = [
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
        ]

        interests = st.multiselect(
            "Your interests",
            interest_options,
            default=profile.get("interests", []),
        )

        career_goal = st.text_input(
            "Career goal",
            value=profile.get("career_goal", ""),
            placeholder="e.g. AI Engineer",
        )

    if st.button(
        "💾 Save My Profile",
        key="save_profile",
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
        dedent(
            """
            <div class="page-heading">
                <div class="eyebrow">AI ADVISOR</div>
                <h1>Your personalized recommendations</h1>
                <p>
                    Based on your academic profile, interests and goals.
                </p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    if not st.session_state.profile:

        st.markdown(
            dedent(
                """
                <div class="empty-state">
                    <div class="empty-icon">👤</div>
                    <h2>Complete your profile first</h2>
                    <p>
                        Tell us about your Intermediate subjects,
                        interests, budget and career goals.
                    </p>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        if st.button(
            "Create My Profile",
            key="create_profile",
            type="primary",
        ):
            navigate("Profile")
            st.rerun()

    else:

        profile = st.session_state.profile

        st.markdown(
            dedent(
                f"""
                <div class="profile-summary">
                    <strong>{profile.get("name", "Student")}</strong>
                    <span>{profile.get("education", "")}</span>
                    <span>{profile.get("percentage", 0)}%</span>
                    <span>{profile.get("location", "")}</span>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        if st.button(
            "✨ Generate My Recommendations",
            key="generate_recommendations",
            use_container_width=True,
            type="primary",
        ):

            with st.spinner("Analyzing your profile..."):
                result = get_recommendations(profile)

            st.markdown(
                '<div class="ai-result">',
                unsafe_allow_html=True,
            )

            st.markdown(result)

            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )


# =========================================================
# AI CHAT
# =========================================================

elif st.session_state.page == "AI Chat":

    st.markdown(
        dedent(
            """
            <div class="page-heading">
                <div class="eyebrow">EDUPATH AI</div>
                <h1>Ask anything about your next step</h1>
                <p>
                    Ask about degrees, careers, universities,
                    admissions, scholarships or entrance tests.
                </p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    for message in st.session_state.chat_history:

        if message["role"] == "user":

            st.markdown(
                dedent(
                    f"""
                    <div class="chat-user">
                        {message["content"]}
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )

        else:

            st.markdown(
                dedent(
                    f"""
                    <div class="chat-ai">
                        <strong>🤖 EduPath AI</strong>
                        <br><br>
                        {message["content"]}
                    </div>
                    """
                ),
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
# AI AGENT
# =========================================================

elif st.session_state.page == "AI Agent":

    st.markdown(
        dedent(
            """
            <div class="page-heading">
                <div class="eyebrow">AGENTIC AI</div>
                <h1>Let EduPath work through the problem</h1>
                <p>
                    The agent can research, compare and prepare
                    plans for you.
                </p>
            </div>
            """
        ),
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
            key="run_agent",
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
                dedent(
                    """
                    <div class="agent-label">
                        🧠 AGENT RESULT
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )

            st.markdown(
                st.session_state.agent_result
            )

            st.markdown(
                dedent(
                    """
                    <div class="confirmation-box">
                        <strong>Before you take action</strong><br>
                        Review the recommendations carefully.
                        EduPath AI does not automatically submit
                        applications or make consequential decisions
                        for you.
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )

            c1, c2 = st.columns(2)

            with c1:

                if st.button(
                    "❤️ Save Result",
                    key="save_agent_result",
                    use_container_width=True,
                ):

                    st.session_state.saved.append(
                        st.session_state.agent_result
                    )

                    st.success("Saved!")

            with c2:

                if st.button(
                    "Clear",
                    key="clear_agent_result",
                    use_container_width=True,
                ):

                    st.session_state.agent_result = None
                    st.rerun()


# =========================================================
# EXPLORE
# =========================================================

elif st.session_state.page == "Explore":

    st.markdown(
        dedent(
            """
            <div class="page-heading">
                <div class="eyebrow">EXPLORE</div>
                <h1>Discover your opportunities</h1>
                <p>
                    Explore sample Pakistani education opportunities.
                </p>
            </div>
            """
        ),
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
                dedent(
                    f"""
                    <div class="listing-card">
                        <h3>🏫 {university["name"]}</h3>

                        <p>
                            {university["city"]} · {university["type"]}
                        </p>

                        <p>
                            <strong>Programs:</strong>
                            {", ".join(university["programs"])}
                        </p>
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )

    elif category == "Degrees":

        for degree in get_degrees():

            st.markdown(
                dedent(
                    f"""
                    <div class="listing-card">
                        <h3>🎓 {degree["name"]}</h3>
                        <p>{degree["description"]}</p>
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )

    elif category == "Scholarships":

        for scholarship in get_scholarships():

            st.markdown(
                dedent(
                    f"""
                    <div class="listing-card">
                        <h3>💰 {scholarship["name"]}</h3>
                        <p>{scholarship["description"]}</p>
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )

    else:

        for test in get_entrance_tests():

            st.markdown(
                dedent(
                    f"""
                    <div class="listing-card">
                        <h3>📝 {test["name"]}</h3>
                        <p>{test["description"]}</p>
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )


# =========================================================
# SAVED
# =========================================================

elif st.session_state.page == "Saved":

    st.markdown(
        dedent(
            """
            <div class="page-heading">
                <div class="eyebrow">MY SPACE</div>
                <h1>Saved opportunities</h1>
                <p>
                    Keep useful recommendations in one place.
                </p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    if not st.session_state.saved:

        st.markdown(
            dedent(
                """
                <div class="empty-state">
                    <div class="empty-icon">🔖</div>
                    <h2>Nothing saved yet</h2>
                    <p>
                        Your saved universities, scholarships and
                        plans will appear here.
                    </p>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    else:

        for item in st.session_state.saved:

            st.markdown(
                dedent(
                    f"""
                    <div class="listing-card">
                        {item}
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )
