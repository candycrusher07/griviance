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

    /* Text Area for grievance form */
    .stTextArea > div > textarea {
        background-color: #fff8fc !important;
        color: #4a0033 !important;
        font-family: 'Georgia', serif !important;
    }
    
   <style>
/* Global label styling - affects all form labels */
label, .css-1cpxqw2, .css-1d391kg {
    color: #b30059 !important;        /* Romantic deep rose color */
    font-weight: bold;
    font-family: 'Georgia', serif;
}

/* Text input background and border styling */
.stTextInput > div > div > input {
    background-color: #fff8e1 !important;  /* Buttery yellow */
    color: #5e3700 !important;             /* Deep brown text */
    border: 2px solid #ffd54f !important;  /* Golden border */
    border-radius: 10px;
    font-family: 'Georgia', serif;
}

/* Text area customization (for "What's bothering you?") */
.stTextArea > div > textarea {
    background-color: #fce4ec !important;  /* Soft pink */
    color: #880e4f !important;             /* Deep rose text */
    border: 2px solid #f06292 !important;  /* Pink border */
    border-radius: 10px;
    font-family: 'Georgia', serif;
}

/* Select boxes (for Mood, Severity) */
.stSelectbox > div > div {
    background-color: #f3e5f5 !important;  /* Lavender */
    color: #4a148c !important;             /* Deep purple text */
    border: 2px solid #ba68c8 !important;
    border-radius: 10px;
    font-family: 'Georgia', serif;
}



    /* Button styling */
    .stButton>button {
        background-color: #ff66a3 !important;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-family: 'Georgia', serif;
        font-weight: bold;


    /* Login input boxes (username & password) */
    .stTextInput > div > div > input {
        background-color: #ffe6f0 !important;
        color: #800040 !important;
        font-family: 'Georgia', serif !important;
        border-radius: 8px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #ff3385 !important;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }

    /* Confirmation box styling */
    .confirmation-box {
        background-color: #d1ffe6;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #00cc88;
        text-align: center;
        margin-top: 20px;
        color: #006644;
    }

    /* Input & Text Area */
    .stTextInput > div > div > input,
    .stTextArea > div > textarea {
        background-color: #ffe6f0 !important;
        color: #660033 !important;
        font-family: 'Georgia', serif;
        border: 2px solid #ff99cc;
        border-radius: 10px;
    }

    /* Select Box (Dropdown) */
    .stSelectbox > div > div,
    .stSelectbox label {
        background-color: #fff0f5 !important;
        color: #800040 !important;
        font-family: 'Georgia', serif;
    }

    /* Slider */
    .stSlider > div {
        background-color: #ffd9ec !important;
        padding: 10px;
        border-radius: 10px;
    }

    /* Submit and Logout Buttons */
    .stButton > button {
        background-color: #ff66a3 !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: bold;
        font-family: 'Georgia', serif;
    }

    /* Custom dialog box */
    .confirmation-box {
        background-color: #ccf5ff; /* CONTRASTING pastel blue */
        color: #00334d;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #66d9ff;
        text-align: center;
        margin-top: 20px;
        font-family: 'Georgia', serif;
    }

    /* Streamlit's alert boxes override (success, warning, error) */
    .stAlert {
        background-color: #ffe0ec !important;
        border-left: 5px solid #ff3385 !important;
        color: #800040 !important;
        font-family: 'Georgia', serif;
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
