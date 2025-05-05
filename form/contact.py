import streamlit as st
import re
import requests

# --- Load webhook URL from secrets.toml ---
WEBHOOK_URL = st.secrets.get("WEBHOOK_URL")  # You’ll set this in .streamlit/secrets.toml

# --- Basic email validator using regex ---
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

# --- Contact form logic ---
def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send Message")

    if submit:
        # --- Validation ---
        if not name:
            st.error("Please enter your name.", icon="🧑")
            st.stop()
        if not email:
            st.error("Please enter your email address.", icon="📧")
            st.stop()
        if not is_valid_email(email):
            st.error("Please enter a valid email address.", icon="⚠️")
            st.stop()
        if not message:
            st.error("Please enter your message.", icon="💬")
            st.stop()
        if not WEBHOOK_URL:
            st.error("Webhook is not configured. Please try again later.", icon="🚫")
            st.stop()

        # --- Prepare payload ---
        payload = {
            "name": name,
            "email": email,
            "message": message
        }

        # --- Send to webhook (e.g., Pabbly, Zapier, Make.com) ---
        try:
            st.caption(f"🔗 Webhook URL loaded: {WEBHOOK_URL}")
            st.write("DEBUG:", WEBHOOK_URL)
            response = requests.post(WEBHOOK_URL, json=payload)
            if response.status_code == 200:
                st.success("🎉 Your message was sent successfully!", icon="✅")
            else:
                st.error("There was a problem sending your message. Please try again later.", icon="😕")
        except Exception as e:
            st.error(f"Error sending message: {e}", icon="❌")
