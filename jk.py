import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =============================
# Page Configuration
# =============================
st.set_page_config(page_title="Boyfriend Grievance Portal", layout="centered")

# =============================
# Credentials
# =============================
CORRECT_USERNAME = "sadiyah"
CORRECT_PASSWORD = "pandu123"

# =============================
# Email Configuration
# =============================
SENDER_EMAIL = "urghbabe1810@gmail.com"  # Replace with your email
SENDER_PASSWORD = "xfbw rrkz svrmm zcqj"  # App password
RECEIVER_EMAIL = "aamirtauhid07@example.com"  # Replace with actual receiver email

def send_grievance_email(title, grievance, mood, severity, solution):
    """Send email when grievance is submitted."""
    subject = f"Grievance Submitted: {title}"
    body = f"""
    💌 A new grievance has been submitted:

    Title: {title}
    What's bothering you: {grievance}
    Mood: {mood}
    Severity (1-10): {severity}
    Suggested Solution: {solution}
    """

    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        server.quit()
    except Exception as e:
        st.warning(f"Failed to send email: {e}")

# =============================
# Custom CSS (Contrast & Style)
# =============================
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f5;
    }
    h1, h3 {
        color: #cc0066;
        font-family: 'Georgia', serif;
    }
    label, .stTextInput>div>div>input {
        color: #800040;
        font-family: 'Georgia', serif;
    }
    .stTextArea>div>textarea {
        background-color: #fff8fc;
        color: #4a0033;
        font-family: 'Georgia', serif;
    }
    .stButton>button {
        background-color: #ff3385 !important;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }
    .confirmation-box {
        background-color: #d1ffe6;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #00cc88;
        text-align: center;
        margin-top: 20px;
        color: #006644;
    }
    </style>
""", unsafe_allow_html=True)

# =============================
# Session Initialization
# =============================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =============================
# Login Page
# =============================
def login_page():
    st.title("💕 Boyfriend Grievance Portal - Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            st.session_state.logged_in = True
            st.success("Welcome back, Sadiyah 💖")
        else:
            st.error("Wrong username or password 😢")

# =============================
# Grievance Form Page
# =============================
def grievance_form():
    st.title("💌 Express Your Heart")

    title = st.text_input("Title")
    grievance = st.text_area("What's bothering you?")
    mood = st.selectbox("Mood", ["Happy 😊", "Sad 😢", "Angry 😡", "Disappointed 😞", "Confused 🤔"])
    severity = st.slider("How serious is it?", 1, 10)
    solution = st.selectbox("What might make it better?", ["Chocolates 🍫", "Chicken Strips 🍗", "Corner House 🍨", "McD 🍔", "WhiteHouse 🏠"])

    if st.button("Submit Grievance"):
        if title and grievance:
            st.markdown(f"""
                <div class="confirmation-box">
                    <h3>💗 Your grievance has been submitted!</h3>
                    <p>Aamir will respond soon with love and care 💌✨</p>
                </div>
            """, unsafe_allow_html=True)
            send_grievance_email(title, grievance, mood, severity, solution)
        else:
            st.warning("Please complete all the fields 🙏")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# =============================
# Main App Logic
# =============================
def main():
    if st.session_state.logged_in:
        grievance_form()
    else:
        login_page()

if __name__ == "__main__":
    main()
