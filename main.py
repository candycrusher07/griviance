import streamlit as st
import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials (replace with your info)
SENDER_EMAIL = "urghbabe1810@gmail.com"
SENDER_PASSWORD = "xfbw rrkz svmm zcqj"
RECEIVER_EMAIL = "aamirtauhid07@gmail.com"

# Login system
users = {
    "sadiyah": "pandu123"
}

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Email sending function
def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# Romantic pastel pink styling
st.markdown("""
    <style>
    .stApp {
        background-color: #ffe6f0;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    h1, h3, label, .stTextInput label, .stTextArea label, .stSelectbox label {
        color: #800040;
        font-weight: bold;
    }
    .stTextInput > div > div > input,
    .stTextArea > div > textarea,
    .stSelectbox > div,
    .stSlider > div {
        background-color: #fff0f5 !important;
        color: #4d0033 !important;
    }
    .stButton > button {
        background-color: #ff66a3 !important;
        color: white;
        border-radius: 12px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


# Login screen
if username in users and users[username] == password:
    st.session_state.logged_in = True
    st.success("Logged in successfully 💗")
else:
    st.error("Invalid credentials 💔")


# Grievance form
def grievance_form():
    st.markdown("<h1>💌 Express Your Heart</h1>", unsafe_allow_html=True)

    title = st.text_input("Title of Your Complaint")
    grievance = st.text_area("What's bothering you, love?")
    mood = st.selectbox("Your Mood", ["Sad 😢", "Angry 😡", "Disappointed 😞", "Ignored 😶", "Hopeless 😔"])
    severity = st.slider("How serious is it?", 1, 10)
    solutions = st.selectbox("Chocolates", "Chicken Strips", "Corner House", "Mcd", "WhiteHouse")

    if st.button("Send to the universe 💌"):
        st.markdown(
            """
            <div style='background-color:#ffd6e7;padding:20px;border-radius:10px;border:2px solid #ff80bf'>
            <h3>Your grievance has been submitted 💖</h3>
            <p>Aamir will get back to you shortly 💌✨</p>
            <p>He will think about it!!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        subject = f"New Grievance: {title}"
        body = f"""
Title: {title}
Mood: {mood}
Severity: {severity}/10
Complaint: {grievance}
Suggested Solutions: {solutions}
"""
        send_email(subject, body)

# Run app
if not st.session_state.logged_in:
    login()
else:
    grievance_form()
