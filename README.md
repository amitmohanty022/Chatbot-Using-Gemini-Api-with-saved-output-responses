# Gemini Q&A Chatbot with Saved Chat History

A Streamlit chatbot powered by Google Gemini that streams answers and keeps the full conversation history on screen for the session.

## 🔗 Live demo

Not hosted yet. Deploy it for free on Streamlit Community Cloud: click the badge (or go to https://share.streamlit.io → **Create app**) and use repository `amitmohanty022/Chatbot-Using-Gemini-Api-with-saved-output-responses`, branch `main`, main file `qnapp.py`.

[![Deploy on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=amitmohanty022/Chatbot-Using-Gemini-Api-with-saved-output-responses&branch=main&mainModule=qnapp.py)

On the Streamlit deploy page, add `GOOGLE_API_KEY` under **Advanced settings → Secrets**.

## Features

- Streaming responses from Gemini
- Multi-turn chat: the model remembers earlier questions in the session
- Chat history shown below every answer

## Tech stack

Python, Streamlit, Google Gen AI SDK (`google-genai`), Gemini 3.8 Flash

## Run locally

```bash
git clone https://github.com/amitmohanty022/Chatbot-Using-Gemini-Api-with-saved-output-responses.git
cd Chatbot-Using-Gemini-Api-with-saved-output-responses
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file (or add the same keys to **Streamlit secrets** when deploying):

```env
GOOGLE_API_KEY=your_gemini_api_key   # get one at https://aistudio.google.com/apikey
# optional, defaults to gemini-3.8-flash
GEMINI_MODEL=gemini-3.8-flash
```

Then start the app:

```bash
streamlit run qnapp.py
```

## Author

**Amit Kumar Mohanty** · [GitHub](https://github.com/amitmohanty022) · [LinkedIn](https://www.linkedin.com/in/amitkrmohanty/)
