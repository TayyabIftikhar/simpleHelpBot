import streamlit as st
import os
import time
from log import log_interaction

st.markdown("""
<style>
    /* App background with soft pattern and subtle gradient */
    .stApp {
        background: repeating-linear-gradient(
            45deg,
            #C6E2FF,
            #C6E2FF 20px,
            #d9ecff 20px,
            #d9ecff 40px
        );
        color: black;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title bar with deep navy and glow effect */
    h1 {
        background-color: #074880;
        color: white !important;
        padding: 0.6rem 1rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        text-align: center;
        letter-spacing: 1px;
    }

    /* Logo container styling */
    img {
        background-color: #074880;
        padding: 0.4rem;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }

    /* Buttons */
    .stButton>button {
        background-color: #074880;
        color: white;
        border-radius: 8px;
        padding: 0.4rem 1rem;
        font-weight: 600;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #055072;
        transform: scale(1.03);
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }

    /* Dropdowns and input text */
    label, .stSelectbox label, .stTextInput label {
        color: black !important;
        font-weight: 600;
    }

    .stSelectbox div[data-baseweb="select"] {
        border: 1px solid #074880;
        border-radius: 8px;
        background-color: #ffffff;
    }

    /* Answer box styling */
    .stMarkdown div[style*="background: #f4f6fa"] {
        background: #ffffff;
        border-left: 5px solid #074880;
        padding: 1rem;
        color: black;
        border-radius: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        font-size: 1rem;
        line-height: 1.6;
    }

    /* Footer text */
    footer, .footer {
        color: #074880;
        font-size: 0.95rem;
        margin-top: 2em;
    }
</style>
""", unsafe_allow_html=True)


def get_data_folders(path="data"):
    try:
        return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    except Exception:
        return []

st.set_page_config(page_title="NUST HELP BOT", page_icon="nust_logo.png", layout="centered")

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.image("nust_logo.png", width=100, output_format="PNG")

st.markdown("<div style='margin-top: -40px;'></div>", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; font-size: 2.5rem; font-weight: 700; letter-spacing: 1px; margin-top: 0;'>NUST HELP BOT</h1>
""", unsafe_allow_html=True)



col1, col2 = st.columns(2)

with col2:
    st.markdown("<div style='font-size: 1.1rem; margin-bottom: 0.3em;'>Select Program:</div>", unsafe_allow_html=True)
    data_folders = get_data_folders("data")
    def to_option(name):
        return name.replace('_', ' ')
    options = [to_option(name) for name in data_folders]
    selected_bot = st.selectbox("Select Program", options, label_visibility="collapsed", key="bot_select",
        help="Choose a bot (from data folders)")

with col1:
    st.markdown("<div style='font-size: 1.1rem; margin-bottom: 0.3em;'>Select University:</div>", unsafe_allow_html=True)
    ships = ["NUST"]
    selected_ship = st.selectbox("Select University", ships, label_visibility="collapsed", key="ship_select",
        help="Choose a university (currently only NUST is available)")


from db_utils import get_or_build_bot_db_path
from query_data import query_rag

if "answer" not in st.session_state:
    st.session_state["answer"] = ""

user_input = st.text_input("Type your message:", placeholder="Type your message...", key="input", label_visibility="collapsed")
send_clicked = st.button("Send", key="send_btn", use_container_width=False)

if send_clicked and user_input.strip():
    folder_map = {to_option(name): name for name in data_folders}
    folder_name = folder_map.get(selected_bot)
    if folder_name:
        with st.spinner("Checking/Building knowledge base for selected bot..."):
            db_path = get_or_build_bot_db_path(folder_name)
        with st.spinner("Thinking..."):
            start_time = time.time()
            answer = query_rag(user_input, db_path)
            end_time = time.time()
            time_taken = round(end_time - start_time, 3)
            log_interaction(user_input, answer, time_taken)

        st.session_state["answer"] = answer
    else:
        st.session_state["answer"] = "Could not find selected bot's folder."

if st.session_state["answer"]:
    st.markdown(f"<div style='background: #f4f6fa; border-radius: 8px; padding: 0.8em; margin-bottom: 1.5em;'>{st.session_state['answer']}</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size: 1rem; margin-top: 2em;'>
    This is an alpha version of this software, Developed at <b>HPC Lab, NUST-SEECS</b><br>
    <span style='font-size:0.9rem;'><a href='#' style='color:#0066cc;'></a></span>
</div>
""", unsafe_allow_html=True)
