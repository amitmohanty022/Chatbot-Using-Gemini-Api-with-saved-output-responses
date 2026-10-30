import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

st.set_page_config(page_title="Q&A Demo")
st.header("GEMINI LLM APPLICATION")

if not API_KEY:
    st.error("GOOGLE_API_KEY is not set. Copy .env.example to .env and paste your Gemini API key.")
    st.stop()


# Keep one client and one chat session per browser session so the model
# remembers earlier questions.
if "chat" not in st.session_state:
    client = genai.Client(api_key=API_KEY)
    st.session_state["chat"] = client.chats.create(model=MODEL)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


def get_gemini_response(question):
    return st.session_state["chat"].send_message_stream(question)


user_input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    response = get_gemini_response(user_input)
    st.session_state["chat_history"].append(("You", user_input))
    st.subheader("The Response is")
    full_answer = ""
    placeholder = st.empty()
    for chunk in response:
        if chunk.text:
            full_answer += chunk.text
            placeholder.markdown(full_answer)
    st.session_state["chat_history"].append(("Bot", full_answer))

st.subheader("The Chat history is")

for role, text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")
