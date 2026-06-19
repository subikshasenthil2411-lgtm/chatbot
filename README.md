# 🤖 AI Personal Assistant Chatbot

A full-stack chatbot app using Flask (backend) + HTML/CSS/JS (frontend) powered by Claude AI.

---

## 📁 Project Structure

```
chatbot-app/
├── app.py              ← Flask backend (API server)
├── requirements.txt    ← Python dependencies
├── static/
│   └── index.html      ← Frontend chat UI
└── README.md
```

---

## 🚀 Setup & Run

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Set your API key
Get your key from https://console.anthropic.com

**Option A: Environment variable (recommended)**
```bash
# Mac/Linux
export ANTHROPIC_API_KEY="sk-ant-..."

# Windows
set ANTHROPIC_API_KEY=sk-ant-...
```

**Option B: Edit app.py directly**
```python
client = anthropic.Anthropic(api_key="sk-ant-your-key-here")
```

### Step 3 — Run the server
```bash
python app.py
```

### Step 4 — Open in browser
```
http://localhost:5000
```

---

## 🔧 Customization

### Change the bot's personality
Edit the system prompt in `app.py`:
```python
system_prompt = "You are a helpful customer support agent for Acme Corp..."
```
Or change it live in the UI using the "Personality" bar at the top.

### Change the model
In `app.py`, replace `claude-sonnet-4-6` with any Anthropic model.

---

## ☁️ Deploy to the Web

### Render (Free)
1. Push code to GitHub
2. Go to https://render.com → New Web Service
3. Connect your repo
4. Set `ANTHROPIC_API_KEY` as an environment variable
5. Set start command: `python app.py`

### Railway
1. Push to GitHub
2. Go to https://railway.app → New Project → Deploy from GitHub
3. Add `ANTHROPIC_API_KEY` as an env variable

---

## 📡 API Endpoint

**POST** `/chat`

Request body:
```json
{
  "messages": [
    {"role": "user", "content": "Hello!"}
  ],
  "system": "You are a helpful assistant."
}
```

Response:
```json
{
  "reply": "Hello! How can I help you today?"
}
```
