import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =============================
# Configure Streamlit page
# =============================
st.set_page_config(page_title="Boyfriend Grievance Portal", layout="centered")

# =============================
# HARD CODED CREDENTIALS
# =============================
CORRECT_USERNAME = "sadiyah"
CORRECT_PASSWORD = "pandu123"

# =============================
# EMAIL CONFIGURATION (Update these values)
# =============================
SENDER_EMAIL = "urghbabe1810@gmail.com"      # Replace with your sender email
SENDER_PASSWORD = "xfbw rrkz svrmm zcqj"               # Replace with your Gmail App Password or SMTP password
RECEIVER_EMAIL = "aamirtauhid07@example.com"      # Replace with the email where you want to receive notifications

def send_grievance_email(title, grievance, mood, severity_solutions):
    """Send an email notification when a grievance is submitted."""
    subject = f"New Grievance Submitted: {title}"
    body = f"""
    A new grievance has been submitted on the Boyfriend Grievance Portal.

    Title: {title}
    What's bothering you: {grievance}
    Mood: {mood}
    Severity & Suggested Solutions: {severity_solutions}
    """

    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Using SMTP_SSL for security on port 465
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        server.quit()
    except Exception as e:
        st.warning(f"Email notification failed: {e}")

# =============================
# CUSTOM CSS FOR ROMANTIC, PASTEL DESIGN
# =============================
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f5;
    }
    h1, h2, h3 {
        color: #cc3366;
        font-family: 'Georgia', serif;
    }
    label, .css-1cpxqw2, .stTextInput>div>div>input {
        color: #800040;
        font-family: 'Georgia', serif;
    }
    .stTextArea>div>textarea {
        background-color: #ffe6f0 !important;
        color: #800040;
        font-family: 'Georgia', serif;
    }
    .stButton>button {
        background-color: #ff66a3 !important;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }
    .confirmation-box {
        background-color: #ffd6e7;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #ff80bf;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# =============================
# INITIALIZE SESSION STATE
# =============================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =============================
# LOGIN PAGE
# =============================
def login_page():
    st.title("💕 Boyfriend Grievance Portal - Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful! Welcome, sadiyah!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password. Please try again.")

# =============================
# GRIEVANCE FORM PAGE
# =============================
def grievance_form():
    st.title("💌 Express Your Heart")
    
    # Form fields
    title = st.text_input("Title")
    grievance = st.text_area("What's bothering you?")
    mood = st.selectbox("Mood", ["Happy 😊", "Sad 😢", "Angry 😡", "Disappointed 😞", "Confused 🤔"])
    severity_solutions = st.text_area("Severity (scale 1-10) & Suggested Solutions")
    
    if st.button("Submit Grievance"):
        if title and grievance and mood and severity_solutions:
            st.markdown("""
                <div class="confirmation-box">
                    <h3>Your grievance has been submitted 💖</h3>
                    <p>Love always finds a way. 💌✨</p>
                </div>
                """, unsafe_allow_html=True)
            # Send email notification with the grievance details
            send_grievance_email(title, grievance, mood, severity_solutions)
        else:
            st.warning("Please fill out all the fields.")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# =============================
# MAIN APP LOGIC
# =============================
def main():
    if st.session_state.logged_in:
        grievance_form()
    else:
        login_page()

if __name__ == "__main__":
    main()
