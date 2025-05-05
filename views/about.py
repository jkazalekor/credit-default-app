import streamlit as st
from form.contact import contact_form  # import the form logic

# --- MODAL FORM USING EXPERIMENTAL DIALOG ---
@st.dialog("📬 Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION (Profile + Summary) ---
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.image("assets/jkazalekor image streamlit.jpg", width=220)  # Replace with your actual image

with col2:
    st.title("Joseph Kwami Azalekor", anchor=False)
    st.write(
        "Machine Learning Enthusiast • Data Analyst • Passionate about turning models into products."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("📈 Experience & Qualifications", anchor=False)
st.markdown("""
- 3+ years experience in data analysis and machine learning  
- Skilled in Python, Streamlit, and AWS  
- Solid grasp of model deployment and MLOps fundamentals  
- Passionate about end-to-end ML product development
""")

# --- TECHNICAL SKILLS ---
st.write("\n")
st.subheader("🧠 Hard Skills", anchor=False)
st.markdown("""
- **Programming**: Python (Pandas, Scikit-learn, XGBoost), SQL  
- **Deployment**: Streamlit, AWS Lambda, API Gateway  
- **Visualization**: Matplotlib, Plotly, Power BI  
- **Databases**: PostgreSQL, SQLite, MongoDB
""")
