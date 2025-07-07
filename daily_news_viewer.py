import streamlit as st
from datetime import datetime
import requests

# --- Set page config FIRST ---
st.set_page_config(page_title="Dhurin News Feed Viewer", layout="wide")

# --- Custom CSS for background and sidebar styling ---
st.markdown(
    """
    <style>
    /* Background image */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1497493292307-31c376b6e479?auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Style sidebar */
    .css-1d391kg {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 1.5rem;
        border-radius: 10px;
    }

    /* Calendar and link styling */
    .stDateInput>div>div {
        font-weight: bold;
        font-size: 1.1rem;
        color: #333;
    }
    .sidebar-content a {
        font-size: 1rem;
        color: #0066cc;
        text-decoration: underline;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- App title and sidebar ---
st.markdown(
    """
    <div style='background-color:#f0f0f0; padding: 1rem 2rem; border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.15); margin-bottom: 2rem;'>
        <h1 style='color:#3f51b5; font-size: 4rem; margin: 0;'>📰 Dhurin Daily News Feed</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Sidebar calendar to select date ---
selected_date = st.sidebar.date_input("Select a date", datetime.today())

# --- Format date to match your HTML filenames ---
formatted_date = selected_date.strftime('%d%b%Y')  # e.g., 22Nov2024
html_filename = f"daily_news_feed_{formatted_date}.html"
github_url = f"https://ritabratadasBigO.github.io/Daily-News-Feed/{html_filename}"

st.sidebar.markdown(f"[🔗 View raw HTML on GitHub]({github_url})")

# --- Try to fetch the HTML content ---
try:
    response = requests.get(github_url)
    if response.status_code == 200:
        st.components.v1.html(response.text, height=1200, scrolling=True)
    else:
        st.markdown(
            f"<div style='color:black; font-weight:bold; font-size:1.3rem;'>⚠️ No news feed available for {selected_date.strftime('%A, %d %B %Y')} (HTTP Status: {response.status_code})</div>",
            unsafe_allow_html=True
        )
except Exception as e:
    st.markdown(
        f"<div style='color:black; font-weight:bold; font-size:1.3rem;'>🚫 Failed to load the news feed. Error: {e}</div>",
        unsafe_allow_html=True
    )