from dotenv import load_dotenv

load_dotenv()

import os

import streamlit as st
from google import genai


def get_api_key():
    """Read the Gemini API key from Streamlit secrets or the environment."""
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            return st.secrets["GOOGLE_API_KEY"]
    except Exception:
        pass
    return os.getenv("GOOGLE_API_KEY")


MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


def get_chat():
    """Keep one Gemini chat session per browser session so the model remembers context."""
    if "gemini_chat" not in st.session_state:
        client = genai.Client(api_key=get_api_key())
        st.session_state["gemini_chat"] = client.chats.create(model=MODEL_NAME)
    return st.session_state["gemini_chat"]


def get_gemini_response(question):
    return get_chat().send_message_stream(question)


# STREAMLIT APP

st.set_page_config(page_title="Q&A Demo")

st.header("GEMINI LLM APPLICATION")

# CHAT HISTORY IF IT DOES NOT EXIST
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    if not get_api_key():
        st.error("GOOGLE_API_KEY is not set. Add it to a .env file or to Streamlit secrets.")
    else:
        response = get_gemini_response(input)
        # add user query and response to session chat history
        st.session_state["chat_history"].append(("You", input))
        st.subheader("The Response is")
        full_text = ""
        for chunk in response:
            if chunk.text:
                st.write(chunk.text)
                full_text += chunk.text
        st.session_state["chat_history"].append(("Bot", full_text))

st.subheader("The Chat history is")

for role, text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")
