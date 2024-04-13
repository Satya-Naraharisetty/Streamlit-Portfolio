import streamlit as st
# Author: <"Satya Sri Naga Venkat Naraharisetty">
# Date: <"2021-09-30">
# Purpose: <"To create a resume web app using Streamlit">


st.title("Satya Sri Naga Venkat Naraharisetty")
st.markdown("---")
st.write("""A motivated student with strong skills in programming, seeking opportunities to gain practical experience in the IT industry. I am proactive and willing to learn, with a strong work ethic and a passion for Software development. I am
excited to contribute to our organization"s success and continue growing personally and professionally.
""")
st.download_button("Download Resume", "Hello", "Satya\'s Resume.pdf")

def main():

    st.header("Personal Information")
    st.write("Name: Satya Sri Naga Venkat Naraharisetty")
    st.write("Email: venkatnaraharisetty1234@gmail.com")
    st.write("Phone: +917702014320")

    Skills()
    Projects()
    Education()


def Skills():
    st.header("Skills")
    st.write("Java, Python, JavaScript, HTML, CSS, SQL, GIT, Streamlit")


def Education():
    st.header("Education")
    st.write("B.Tech in Electronics and Communication Engineering, Vishnu Institute of Technology, 2020-2024")
    st.write("Intermediate, Aditya Junior College, 2018-2020")
    st.write("SSC, Apollo E.M High School, 2017-2018")


def Projects():
    st.header("Projects")
    st.write("Project 1: Image Restoration Using CNN")
    st.text("This project is about restoring the images using Convolutional Neural Networks.")
    st.write("Project 2: Live Location Updater")
    st.text("This project is about updating the location of the user in real-time.")
    st.table({"data": ["Project 1", "Project 2"], "Description": ["Image Restoration Using CNN", "Live Location Updater"]})

    

if __name__ == "__main__":
    main()




