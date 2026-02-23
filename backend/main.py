from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the FastAPI app
app = FastAPI()

# This allows your website (frontend) to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# This defines what a chat message looks like
class ChatMessage(BaseModel):
    message: str

# This is the AI's personality and knowledge about NexaDesk
SYSTEM_PROMPT = """
You are Lindo, a friendly and professional AI support assistant for Lindoom —
an IT support company. You help users with:

- Common IT troubleshooting (WiFi, passwords, software, hardware)
- Information about NexaDesk services
- Raising support tickets
- General tech questions

NexaDesk Information:
- Support Hours: Monday–Friday, 8AM–8PM EST
- Emergency Support: 24/7 for premium clients
- Services: Remote Support, On-site Support, Network Setup, Cybersecurity, Cloud Solutions
- Contact: support@lindoom.com | Phone: 1-800-LINDOOM
- Ticket System: Users can say "create a ticket" and you guide them

Rules:
- Always be helpful, calm, and professional
- If you don't know something, say you'll escalate to a human agent
- Keep answers concise and clear
- For serious issues, always recommend contacting a human agent
"""

# Store conversation history per session (simple in-memory storage)
conversation_history = []

# This is your API endpoint — the URL your website will call
@app.post("/chat")
async def chat(chat_message: ChatMessage):
    # Add the user's message to history
    conversation_history.append({
        "role": "user",
        "parts": [chat_message.message]
    })

    # Send to Gemini with the system prompt
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT
    )

    chat_session = model.start_chat(history=conversation_history[:-1])
    response = chat_session.send_message(chat_message.message)
    reply = response.text

    # Add AI response to history
    conversation_history.append({
        "role": "model",
        "parts": [reply]
    })

    return {"reply": reply}

# A simple test route to check if the server is running
@app.get("/")
async def root():
    return {"status": "Lindoom backend is running!"}