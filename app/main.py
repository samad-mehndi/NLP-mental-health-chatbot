# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import generate_response

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

app = FastAPI(title="Mental Health Chatbot")

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = generate_response(request.message)
    return ChatResponse(response=reply)
