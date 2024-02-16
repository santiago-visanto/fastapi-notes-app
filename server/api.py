from fastapi import FastAPI
from .routes import router as NoteRouter

app = FastAPI()

app.include_router(NoteRouter, prefix="/note")