# AI Voice Mediator 🤖🎤

## What is this?  

A next-level AI agent that listens, feels, and *calmly* mediates heated conversations in real-time voice chatrooms.  
Two parties arguing? Our AI steps in with balanced, emotion-aware responses — all voiced, all human-like, no more text-only boring bots.  

---

## Features 💥

- **Real-time voice input & output:** Uses WebSockets to stream live voice data.  
- **Emotionally aware:** Analyzes tone and sentiment from voice, not just words, for deep emotional context.  
- **AI-powered mediation:** Google Gemini LLM + LangChain craft balanced, peaceful replies to de-escalate tensions.  
- **Context memory:** Uses Qdrant locally to store conversation embeddings and emotional states for continuity.  
- **Fast & scalable:** Powered by FastAPI backend + Next.js frontend for a smooth UX.  

---

## Tech Stack 🛠️  

| Layer           | Tech & Purpose                     |
|-----------------|----------------------------------|
| Frontend        | Next.js — UI, audio capture & playback, WebSocket client  |
| Backend API     | FastAPI — REST + WebSocket server for real-time comms     |
| AI Core         | Google Gemini (LLM) + LangChain for prompt management     |
| Vector Storage  | Qdrant (local) — Memory & context storage via embeddings  |
| Audio Processing| WebRTC/Web Audio API + Python libs for STT & TTS          |

---

## Getting Started 🚦

### Prerequisites  

- Docker (for Qdrant)  
- Python 3.10+  
- Node.js 18+  

### Setup  

```bash
# Clone repo
git clone https://github.com/yourusername/ai-voice-mediator.git
cd ai-voice-mediator

# Start Qdrant vector DB
docker-compose -f qdrant/compose.yml up -d

# Backend setup
cd server
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend setup (new terminal)
cd ../client
npm install
npm run dev
```

---

## Usage 🎧

- Open the frontend in your browser (`http://localhost:3000`).
- Join the voice chatroom, speak your mind.
- Watch the AI listen, analyze, and reply with voice in real time to mediate your convo like a boss.

---

## Future Plans 🔮

- Multilingual emotion detection and response
- Extend to group chats with multi-party mediation

---

## Contributing 🤝

PRs & issues welcome. Let's make AI mediation a reality!

---

## License 📄

MIT License — Do whatever you want with it, just don’t be toxic 😎

---
