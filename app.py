import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st

# Set page configuration first
st.set_page_config(
    page_title="AI Smart Civic Services Platform",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
        color: white;
    }

    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }

    .header-card {
        background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
        border-radius: 18px;
        padding: 2rem;
        box-shadow: 0 12px 25px rgba(37, 99, 235, 0.18);
        margin-bottom: 1.5rem;
    }

    div.stButton > button {
        border-radius: 10px;
        font-weight: 600;
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(59, 130, 246, 0.2);
    }

    .stTextArea textarea, .stTextInput input, .stSelectbox select {
        border-radius: 10px !important;
        border: 1px solid #cbd5e1 !important;
    }

    .stMetric {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 0.8rem 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

from src.database_manager import DatabaseManager
from src.ai_analyzer import AIAnalyzer
from src.complaint_manager import ComplaintManager

from src.pages.home import show_home
from src.pages.submit_complaint import show_submit_complaint
from src.pages.my_complaints import show_my_complaints
from src.pages.admin import show_admin_dashboard
from src.pages.management import show_complaint_management
from src.pages.analytics import show_analytics
from src.pages.ai_testing import show_ai_testing
from src.pages.about import show_about

if "db_manager" not in st.session_state:
    st.session_state.db_manager = DatabaseManager()

if "ai_analyzer" not in st.session_state:
    st.session_state.ai_analyzer = AIAnalyzer()

if "complaint_manager" not in st.session_state:
    st.session_state.complaint_manager = ComplaintManager(
        st.session_state.db_manager,
        st.session_state.ai_analyzer,
    )

if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.markdown(
    """
    <div style='text-align: center; padding: 1rem 0;'>
        <h2 style='color: white; margin: 0; font-size: 1.5rem; font-weight: 800;'>🏙️ CivicSmart AI</h2>
        <p style='color: #94a3b8; font-size: 0.82rem; margin: 5px 0 0 0;'>Smart City Complaint Hub</p>
    </div>
    <hr style='border-color: #334155; margin: 0 0 1rem 0;'>
    """,
    unsafe_allow_html=True,
)

menu_options = {
    "Home": "🏠 Home",
    "Submit Complaint": "📢 Submit Complaint",
    "My Complaints": "🔍 My Complaints",
    "Admin Dashboard": "📊 Admin Dashboard",
    "Complaint Management": "⚙️ Complaint Management",
    "Analytics": "📈 Analytics",
    "AI Testing": "🧪 AI Testing",
    "About": "🤖 About",
}

current_options = list(menu_options.keys())
default_index = current_options.index(st.session_state.page) if st.session_state.page in current_options else 0
selected_label = st.sidebar.radio(
    "Navigation",
    options=list(menu_options.values()),
    index=default_index,
    label_visibility="collapsed",
)
selected_page = [key for key, value in menu_options.items() if value == selected_label][0]
st.session_state.page = selected_page

st.sidebar.markdown("<br><hr style='border-color: #334155; margin: 10px 0;'>", unsafe_allow_html=True)
st.sidebar.markdown("##### 🟢 System Status")

db_count = st.session_state.db_manager.count_complaints()
st.sidebar.markdown(f"💾 **Database:** Connected ({db_count} records)")

if st.session_state.ai_analyzer.is_trained():
    st.sidebar.markdown("🧠 **AI Models:** Active")
else:
    st.sidebar.markdown("⚠️ **AI Models:** Training / fallback mode")

if st.session_state.page == "Home":
    show_home(st.session_state.db_manager, st.session_state.complaint_manager)
elif st.session_state.page == "Submit Complaint":
    show_submit_complaint(st.session_state.db_manager, st.session_state.complaint_manager)
elif st.session_state.page == "My Complaints":
    show_my_complaints(st.session_state.db_manager, st.session_state.complaint_manager)
elif st.session_state.page == "Admin Dashboard":
    show_admin_dashboard(st.session_state.db_manager, st.session_state.complaint_manager)
elif st.session_state.page == "Complaint Management":
    show_complaint_management(st.session_state.db_manager, st.session_state.complaint_manager)
elif st.session_state.page == "Analytics":
    show_analytics(st.session_state.db_manager, st.session_state.complaint_manager)
elif st.session_state.page == "AI Testing":
    show_ai_testing(st.session_state.db_manager, st.session_state.complaint_manager, st.session_state.ai_analyzer)
elif st.session_state.page == "About":
    show_about()
