# Chatbot Using Gemini API (with saved chat history)

A simple question-and-answer chatbot built with Streamlit and Google Gemini. It streams each answer as it is generated, remembers earlier questions in the same session, and shows the full chat history below the answer.

## How to run (step by step)

You need **Python 3.10 or newer** ([download](https://www.python.org/downloads/)).

**1. Download the project**

```bash
git clone https://github.com/amitmohanty022/Chatbot-Using-Gemini-Api-with-saved-output-responses.git
cd Chatbot-Using-Gemini-Api-with-saved-output-responses
```

**2. Create a virtual environment and activate it**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

**3. Install the requirements**

```bash
pip install -r requirements.txt
```

**4. Add your Gemini API key**

- Get a free key at https://aistudio.google.com/apikey
- Copy `.env.example` to a new file named `.env`
  - Windows: `copy .env.example .env`
  - macOS / Linux: `cp .env.example .env`
- Open `.env` and paste your key after `GOOGLE_API_KEY=`

**5. Start the app**

```bash
streamlit run qnapp.py
```

Your browser opens at http://localhost:8501. Type a question and click **Ask the question**.

## How it works

1. A Gemini chat session (`gemini-3.8-flash` by default) is created once per browser session, so follow-up questions have context.
2. Each answer is streamed and shown as it arrives.
3. Every question and answer is saved in the session and listed under "The Chat history is".

To use a different Gemini model, set `GEMINI_MODEL` in `.env`. Refreshing the page starts a new chat.

## Troubleshooting

| Problem | Fix |
|---|---|
| "GOOGLE_API_KEY is not set" | Make sure the file is named exactly `.env` (not `.env.txt`) and is in the project folder. |
| `streamlit: command not found` | Activate the virtual environment (step 2) first. |
| `404 model not found` | Set `GEMINI_MODEL=gemini-3.6-flash` in `.env`. |
