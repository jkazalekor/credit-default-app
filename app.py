import streamlit as st

st.markdown("""
    <style>
    div.stButton > button:hover {
        color: #fc044c !important;          /* Text color on hover */
        border: 1px solid #fc044c !important; /* Border color on hover */
    }
    </style>
""", unsafe_allow_html=True)

# --- PAGE SETUP ---
prediction_page = st.Page(
    "views/predict.py",
    title="Predict",
    icon=":material/psychology_alt:",
    default=True,
)

about_page = st.Page(
    "views/about.py",
    title="About Me",
    icon=":material/account_circle:",
)

# --- NAVIGATION ---
pg = st.navigation({
    "Main": [prediction_page],
    "Info": [about_page]
})

# --- SHARED CONTENT (applies to all pages) ---
st.logo("assets/logo.png")  # Optional: Replace with your actual logo
st.sidebar.markdown("Made by [JK Azalekor](https://github.com/jkazalekor)")

# --- RUN PAGE ---
pg.run()