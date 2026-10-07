import streamlit as st


def apply_styles():

    st.markdown(
        """
        <style>

        /* ------------------------------
           GLOBAL
        ------------------------------ */

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(99,102,241,0.08),
                    transparent 30%
                ),
                #f8fafc;
            color: #0f172a;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 1rem;
            padding-bottom: 4rem;
        }

        /* Hide default Streamlit chrome */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            background: transparent !important;
        }

        /* ------------------------------
           TOP BAR
        ------------------------------ */

        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 18px 0 10px 0;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .brand-icon {
            width: 45px;
            height: 45px;
            border-radius: 14px;
            background: linear-gradient(
                135deg,
                #4f46e5,
                #7c3aed
            );
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 23px;
            box-shadow:
                0 10px 25px rgba(79,70,229,0.20);
        }

        .brand-name {
            font-size: 20px;
            font-weight: 800;
            color: #111827;
        }

        .brand-tagline {
            font-size: 11px;
            color: #64748b;
        }

        .nav-line {
            height: 1px;
            background: #e2e8f0;
            margin: 8px 0 35px 0;
        }

        /* ------------------------------
           HERO
        ------------------------------ */

        .hero {
            padding: 70px 40px;
            border-radius: 30px;
            background:
                radial-gradient(
                    circle at top right,
                    rgba(129,140,248,0.35),
                    transparent 35%
                ),
                linear-gradient(
                    135deg,
                    #111827,
                    #312e81
                );
            color: white;
            margin-bottom: 18px;
            box-shadow:
                0 25px 60px rgba(15,23,42,0.18);
        }

        .hero-badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 100px;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.16);
            font-size: 13px;
            margin-bottom: 22px;
        }

        .hero h1 {
            font-size: clamp(38px, 6vw, 68px);
            line-height: 1.05;
            letter-spacing: -2px;
            margin: 0;
            color: white;
        }

        .hero h1 span {
            color: #a5b4fc;
        }

        .hero p {
            max-width: 650px;
            font-size: 18px;
            line-height: 1.7;
            color: #dbeafe;
            margin-top: 22px;
        }

        /* ------------------------------
           SECTION
        ------------------------------ */

        .section-title {
            font-size: 25px;
            font-weight: 800;
            margin: 25px 0 18px 0;
        }

        .page-heading {
            margin-bottom: 30px;
        }

        .eyebrow {
            color: #6366f1;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 1.5px;
            margin-bottom: 8px;
        }

        .page-heading h1 {
            font-size: 38px;
            letter-spacing: -1px;
            margin: 0;
        }

        .page-heading p {
            color: #64748b;
            font-size: 16px;
        }

        /* ------------------------------
           CARDS
        ------------------------------ */

        .feature-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 24px;
            min-height: 190px;
            box-shadow:
                0 8px 25px rgba(15,23,42,0.04);
            transition: 0.2s ease;
        }

        .feature-icon {
            font-size: 28px;
            margin-bottom: 15px;
        }

        .feature-card h3 {
            margin: 0 0 8px 0;
            font-size: 17px;
        }

        .feature-card p {
            color: #64748b;
            line-height: 1.6;
            font-size: 14px;
        }

        .listing-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 18px;
            padding: 22px;
            margin-bottom: 14px;
            box-shadow:
                0 5px 20px rgba(15,23,42,0.04);
        }

        .listing-card h3 {
            margin: 0 0 7px 0;
        }

        .listing-card p {
            color: #64748b;
        }

        /* ------------------------------
           PROFILE
        ------------------------------ */

        .profile-summary {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 25px;
        }

        .profile-summary span,
        .profile-summary strong {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 100px;
            padding: 8px 14px;
            font-size: 13px;
        }

        .profile-summary strong {
            color: #4f46e5;
        }

        /* ------------------------------
           INFO / AI
        ------------------------------ */

        .info-banner {
            background: #eef2ff;
            border: 1px solid #c7d2fe;
            border-radius: 18px;
            padding: 18px 20px;
            color: #3730a3;
            line-height: 1.6;
        }

        .ai-result {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 28px;
            margin-top: 20px;
            line-height: 1.7;
            box-shadow:
                0 10px 30px rgba(15,23,42,0.05);
        }

        .agent-label {
            margin-top: 25px;
            color: #6366f1;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 1px;
        }

        .confirmation-box {
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-radius: 16px;
            padding: 18px;
            margin-top: 18px;
            color: #92400e;
            line-height: 1.6;
        }

        /* ------------------------------
           CHAT
        ------------------------------ */

        .chat-user {
            background: #4f46e5;
            color: white;
            padding: 14px 18px;
            border-radius: 18px 18px 5px 18px;
            max-width: 75%;
            margin: 10px 0 10px auto;
        }

        .chat-ai {
            background: white;
            border: 1px solid #e2e8f0;
            padding: 18px;
            border-radius: 18px 18px 18px 5px;
            max-width: 85%;
            margin: 10px auto 10px 0;
        }

        /* ------------------------------
           EMPTY STATE
        ------------------------------ */

        .empty-state {
            text-align: center;
            background: white;
            border: 1px dashed #cbd5e1;
            border-radius: 22px;
            padding: 55px 25px;
        }

        .empty-icon {
            font-size: 45px;
            margin-bottom: 12px;
        }

        .empty-state h2 {
            margin: 0;
        }

        .empty-state p {
            color: #64748b;
        }

        /* ------------------------------
           BUTTONS
        ------------------------------ */

        .stButton > button {
            border-radius: 12px !important;
            min-height: 42px !important;
            font-weight: 700 !important;
            border: 1px solid #e2e8f0 !important;
        }

        /* ------------------------------
           INPUTS
        ------------------------------ */

        .stTextInput input,
        .stNumberInput input,
        .stSelectbox div,
        .stMultiSelect div {
            border-radius: 12px !important;
        }

        /* ------------------------------
           MOBILE
        ------------------------------ */

        @media (max-width: 768px) {

            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .hero {
                padding: 40px 25px;
                border-radius: 22px;
            }

            .hero h1 {
                font-size: 42px;
            }

            .hero p {
                font-size: 16px;
            }

            .page-heading h1 {
                font-size: 30px;
            }

            .chat-user,
            .chat-ai {
                max-width: 95%;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
