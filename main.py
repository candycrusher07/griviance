import streamlit as st
import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials (replace with your info)
SENDER_EMAIL = "urghbabe1810@gmail.com"
SENDER_PASSWORD = "xfbw rrkz svmm zcqj"
RECEIVER_EMAIL = "aamirtauhid07@gmail.com"


# Set page title
st.set_page_config(page_title="Login Page", layout="centered")

# Hardcoded credentials
correct_username = "sadiyah"
correct_password = "pandu123"

def main():
    st.title("Login Portal")

    # Input fields
    username = st.text_input("Enter Username:")
    password = st.text_input("Enter Password:", type="password")

    # Login button
    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Login successful!")
            st.write("Welcome, sadiyah! You are now logged in.")
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()



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
