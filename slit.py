import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# --- Load Assets ---
hello_lottie = (
    "https://lottie.host/d6e4a284-7705-4ce7-9de8-752104fa041d/tsvBc7c4Ll.json"
)
unlock = "https://lottie.host/0c94bf5a-5a1a-4cda-aabc-018e0e4e4868/tXYOK07Wwr.json"
verified = "https://lottie.host/1d6a0b08-d34a-4344-8814-3df2cad1bdd5/N8KBKs1sby.json"

# --- Header Section ---
with st.container():
    st.subheader("Hi, I am Hayden :wave:")
    st.title("A Data Analyst From Germany")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective "
    )
    st.write("[Learn More >](https://www.youtube.com/watch?v=VqgUkExPvLY) ")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What do I do")
        st.write("##")
        st.write(
            """
                This is a list:
                - object 1
                - Object 2
                - OBJECT 3
                - ...
            """
        )
        st.write("[Youtube Tutorial >](https://www.youtube.com/watch?v=)")

    with right_column:
        st_lottie(hello_lottie, height=300, key="hello")

# --- Projects ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(unlock, width=200, key="unlock")
        st_lottie(verified, height=150, key="verified")

    with text_column:
        st.subheader("Integrate Lottie Animations ")
        st.write(
            """
            Learn 
            """
        )
        st.markdown("[Watch Video](https://youtube.com)")

# --- Contact ---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/haydenchung1289@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email Address" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
