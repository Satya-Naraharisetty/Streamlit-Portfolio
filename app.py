from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Satya Sri Naga Venkat Naraharisetty"
PAGE_ICON = ":wave:"
NAME = "Satya Sri Naga Venkat Naraharisetty"
DESCRIPTION = """
A motivated student with strong skills in programming, seeking opportunities to gain practical experience in the IT industry. I am proactive and willing to learn, with a strong work ethic and a passion for Software development. I am
excited to contribute to our organization"s success and continue growing personally and professionally.
"""
EMAIL = "venkatnaraharisetty1234@gmail.com"
SOCIAL_MEDIA = {
    "Instagram": "https://www.instagram.com/_._siddu_._._/",
    "LinkedIn": "https://linkedin.com/in/venkatnaraharisetty",
    "GitHub": "https://github.com/satya-naraharisetty",
    "Twitter": "https://twitter.com/Siddu1994421l",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EDUCATION & QUALIFICATIONS ---
st.write('\n')
st.subheader("EDUCATION & Qulifications")
st.write(
    """
- ✔️ B.Tech in Electronics and Communication Engineering, Vishnu Institute of Technology, 2020-2024
- ✔️ Intermediate, Aditya Junior College, 2018-2020
- ✔️ SSC, Apollo E.M High School, 2017-2018
- ✔️ Strong hands on experience and knowledge in Python and Java
- ✔️ Good understanding of application working and database management
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Java, Python (Numpy, Pandas, Streamlit), SQL
- 🌐 Web Technologies: HTML, CSS, GIT
- 🗄️ Databases: MySQL
"""
)


# --- Activities ---
st.write('\n')
st.subheader("Activities")
st.write("---")

# ---1
st.write("🚧", "**Head of Events for ECE department in Campus | Build Club by IITM**")
st.write("06/2022 - Sep/2023")
st.write(
    """
- ► Team Lead for the Project: Hospital Appointment Booking
- ► Organized and promoted the club for 1 year with 30+ participants in the Vishnu College Society
- ► Acknowledged as the most innovative project idea in the program
"""
)

# ---2
st.write('\n')
st.write("🚧", "**Automating Industrial Robots Bootcamp by APSSDC | Igus Germany – Remote**")
st.write("08/2022 - 11/2022")
st.write(
    """
- ► Learned and practiced the controlling of industrial robots
- ► Automated the control of Robot Arm and Axial Components in the Production/Manufacturing Sector using IGUS Software
- ► Minimized human effort and labor costs by writing code for repetitive tasks
"""
)

# ---3
st.write('\n')
st.write("🚧", "**Team Lead | HackForEt: Hackathon by Unstop**")
st.write("04/2022")
st.write(
    """
- ► Managed a team of 3 members efficiently in a 24-hour hackathon and successfully qualified 2 rounds
- ► Created a project for guiding students in their future academics.
"""
)

# ---4 
st.write('\n')
st.write("🚧", "**Team Lead | Smart India Hackathon (SIH)**")
st.write("04/2022")
st.write(
    """
- ► Created a solution to help patients who are searching for blood donors
- ► Provided a platform to connect blood donors and seekers during emergencies
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")