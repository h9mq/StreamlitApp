import streamlit as st
import pandas as pd
import time as t
from google import genai
from dotenv import load_dotenv
import os

if not st.user.is_logged_in:
    if st.button("Log in with Google"):
        st.login()
    st.stop()
    
st.set_page_config(page_title="Tuwaiq Students", layout="centered")

def two_sum():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            sum_two = (Input_Number_One + Input_Number_Two)
            st.success(f"Result {sum_two}")

def three_sum():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            sum_three = (Input_Number_One + Input_Number_Two + Input_Number_Three)
            st.success(f"Result {sum_three}")    

def four_sum():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    Input_Number_Four = st.number_input("Enter The Four Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            sum_four = (Input_Number_One + Input_Number_Two + Input_Number_Three + Input_Number_Four)
            st.success(f"Result {sum_four}") 

def two_minus():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            minus_two = (Input_Number_One - Input_Number_Two)
            st.success(f"Result {minus_two}")

def three_minus():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            minus_three = (Input_Number_One - Input_Number_Two - Input_Number_Three)
            st.success(f"Result {minus_three}")    

def four_minus():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    Input_Number_Four = st.number_input("Enter The Four Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            minus_four = (Input_Number_One - Input_Number_Two - Input_Number_Three - Input_Number_Four)
            st.success(f"Result {minus_four}")

def two_multi():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            multi_two = (Input_Number_One * Input_Number_Two)
            st.success(f"Result {multi_two}")

def three_multi():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            multi_three = (Input_Number_One * Input_Number_Two * Input_Number_Three)
            st.success(f"Result {multi_three}")    

def four_multi():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    Input_Number_Four = st.number_input("Enter The Four Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            multi_four = (Input_Number_One * Input_Number_Two * Input_Number_Three * Input_Number_Four)
            st.success(f"Result {multi_four}")

def two_dvide():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            dvide_two = (Input_Number_One / Input_Number_Two)
            st.success(f"Result {dvide_two}")

def three_dvide():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            dvide_three = (Input_Number_One / Input_Number_Two / Input_Number_Three)
            st.success(f"Result {dvide_three}")    

def four_dvide():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    Input_Number_Four = st.number_input("Enter The Four Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            dvide_four = (Input_Number_One / Input_Number_Two / Input_Number_Three / Input_Number_Four)
            st.success(f"Result {dvide_four}")


st.sidebar.title("Configuration")

with st.sidebar:        
    box_select = st.selectbox("Select The App ", ["Calculator", "Ai"])
    if box_select == "Calculator":

        select_box = st.selectbox("Select", ["+", "-", "x", "÷"])
        select_box2 = st.selectbox("Select How Many Numbers You Want To Calculate", ["Two", "Three", "Four"])
    
    elif box_select =="H":
        select_box3 = st.selectbox("Select", ["1", "2"])

def calc():
    if select_box =="+":
        if select_box2 =="Two":
            two_sum()
        elif select_box2 =="Three":
            three_sum()
        elif select_box2 =="Four":
            four_sum()

    elif select_box =="-":
        if select_box2 == "Two":
            two_minus()        
        elif select_box2 =="Three":
            three_minus()
        elif select_box2 =="Four":
            four_minus()

    elif select_box =="x":
        if select_box2 == "Two":
            two_multi()        
        elif select_box2 =="Three":
             three_multi()
        elif select_box2 =="Four":
            four_multi()

    elif select_box =="÷":
        if select_box2 == "Two":
            two_dvide()
        elif select_box2 =="Three":
            three_dvide()
        elif select_box2 =="Four":
            four_dvide()

def Ai_Sec():
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        try:
            if "GEMINI_API_KEY" in st.secrets:
                API_KEY = st.secrets["GEMINI_API_KEY"]
            elif "Gemini" in st.secrets and "GEMINI_API_KEY" in st.secrets["Gemini"]:
                API_KEY = st.secrets["Gemini"]["GEMINI_API_KEY"]
        except Exception:
            pass

    if not API_KEY:
        st.error("Missing GEMINI_API_KEY in .env file or Streamlit Secrets.")
        st.stop()

    os.environ["GEMINI_API_KEY"] = API_KEY
    client = genai.Client(api_key=API_KEY)
    MODEL_NAME = "gemini-3.5-flash"

    st.title("🤖 Ai Assistant")
    st.markdown(
        "An Intelligent Assistant Powered By **Gemini** And **Tuwaiq Students**."
    )

    if "history" not in st.session_state:
        st.session_state.history = []

    def get_gemini_response(prompt, uploaded_file=None):
        contents = [prompt]

        if uploaded_file is not None:
            contents.append(
                genai.types.Part.from_bytes(
                    data=uploaded_file.getvalue(),
                    mime_type=uploaded_file.type,
                )
            )

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
        )
        return response.text or "The AI returned an empty response."

    for role, msg in st.session_state.history:
        if role == "user":
            st.markdown(f"**You:** {msg}")
        else:
            st.markdown(f"**🤖 AI Assistant:** {msg}")

    with st.form("ai_chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your message here...")
        send = st.form_submit_button("Send")

    uploaded_file = st.file_uploader(
        "Upload a file for the AI",
        type=["pdf", "png", "jpg", "jpeg", "txt", "csv", "py"],
        accept_multiple_files=False,
    )

    if uploaded_file is not None:
        st.caption(f"Attached: {uploaded_file.name}")

        if uploaded_file.type.startswith("image/"):
            st.image(uploaded_file, caption=uploaded_file.name)

    if send:
        if user_input.strip() or uploaded_file is not None:
            prompt = user_input.strip() or "Describe this uploaded file."

            st.session_state.history.append(("user", prompt))

            with st.spinner("AI Assistant is thinking..."):
                try:
                    reply = get_gemini_response(prompt, uploaded_file)
                except Exception as e:
                    reply = f"Error: {e}"

            st.session_state.history.append(("bot", reply))
            st.rerun()
        else:
            st.warning("Please enter a message or upload a file.")

           



if box_select =="Calculator":
    calc()
elif box_select =="Ai":
    Ai_Sec()

    
st.markdown(f"Welcome! {st.user.name}")
if st.button("Log out"):
    st.logout()


